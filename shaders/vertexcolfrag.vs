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
  float intensity;
  float constant;
  float linear;
  float quadratic;
};

#define NUM_LIGHTS 3
uniform light light_data[NUM_LIGHTS];

vec4 Create_Light(vec3 light_pos, vec3 light_color, vec3 normal, vec3 fragpos, vec3 view_dir, float intensity, float constant, float linear, float quadratic)
{
    // Calcular distancia a la luz
    float distance = length(light_pos - fragpos);
    
    // Atenuación realista
    float attenuation = intensity / (constant + linear * distance + quadratic * (distance * distance));
    
    // Ambient light (más suave)
    float a_strength = 0.05;
    vec3 ambient = a_strength * light_color * attenuation;

    // Diffuse light (Lambert)
    vec3 norm = normalize(normal);
    vec3 light_dir = normalize(light_pos - fragpos);
    float diff = max(dot(norm, light_dir), 0.0);
    vec3 diffuse = diff * light_color * attenuation;

    // Specular (Blinn-Phong para más realismo)
    float s_strength = 0.5;
    vec3 halfway_dir = normalize(light_dir + view_dir);
    float spec = pow(max(dot(norm, halfway_dir), 0.0), 64.0); // Shininess más alta
    vec3 specular = s_strength * spec * light_color * attenuation;

    return vec4(color * (ambient + diffuse + specular), 1.0);
}

void main() {
    vec3 view_dir = normalize(view_pos - fragpos);
    
    // Usar valores por defecto si no están definidos en la estructura
    float intensity = 1.0;
    float constant = 1.0;
    float linear = 0.09;
    float quadratic = 0.032;
    
    frag_color = Create_Light(
        light_data[0].position, 
        light_data[0].color, 
        normal, 
        fragpos, 
        view_dir,
        intensity,
        constant,
        linear,
        quadratic
    );

    // Aplicar textura
    vec4 tex_color = texture(tex, UV);
    frag_color = frag_color * tex_color;
    
    // Gamma correction para más realismo
    float gamma = 2.2;
    frag_color.rgb = pow(frag_color.rgb, vec3(1.0/gamma));
}