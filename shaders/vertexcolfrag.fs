#version 330 core

in vec3 color;
in vec3 normal;
in vec3 fragpos;
in vec3 view_pos;
out vec4 frag_color;

in vec2 UV;
uniform sampler2D tex;

struct light
{
  vec3 position;
  vec3 color;
};

#define NUM_LIGHTS 2
uniform light light_data[NUM_LIGHTS];

vec3 Create_Light(vec3 light_pos, vec3 light_color, vec3 normal, vec3 fragpos, vec3 view_dir)
{
    // Si la luz está apagada (color negro), no contribuir
    if (length(light_color) < 0.1) {
        return vec3(0, 0, 0);
    }
    
    //ambient light
    float a_strength = 0.1;
    vec3 ambient = a_strength * light_color;

    //diffuse light
    vec3 norm = normalize(normal);
    vec3 light_dir = normalize(light_pos - fragpos);
    float diff = max(dot(norm, light_dir), 0);
    vec3 diffuse = diff * light_color;

    //specular
    float s_strength = 0.5;
    vec3 reflect_dir = reflect(-light_dir, norm);
    float spec = pow(max(dot(view_dir, reflect_dir), 0), 32);
    vec3 specular = s_strength * spec * light_color;

    return ambient + diffuse + specular;
}

void main() {
    vec3 view_dir = normalize(view_pos - fragpos);
    
    // Inicializar con luz ambiente mínima
    vec3 result = vec3(0.05, 0.05, 0.05);
    
    // PROCESAR AMBAS LUCES
    for(int i = 0; i < NUM_LIGHTS; i++) {
        result += Create_Light(light_data[i].position, light_data[i].color, normal, fragpos, view_dir);
    }

    // Aplicar textura
    frag_color = vec4(result, 1.0) * texture(tex, UV);
}