#version 330 core

in vec3 position;
in vec3 vertex_color;
in vec3 vertex_normal;
in vec2 vertex_uv;

uniform mat4 projection_mat;
uniform mat4 model_mat;
uniform mat4 view_mat;

out vec3 color;
out vec3 normal;
out vec3 fragpos;
out vec3 view_pos;
out vec2 UV;

// Para tangent space (normal mapping)
out vec3 tangent_light_pos;
out vec3 tangent_view_pos;
out vec3 tangent_frag_pos;

void main() {
    // Posición del fragmento en world space
    fragpos = vec3(model_mat * vec4(position, 1.0));
    
    // Normal en world space (con normalización correcta)
    normal = mat3(transpose(inverse(model_mat))) * vertex_normal;
    
    // Posición de la cámara
    view_pos = vec3(inverse(view_mat)[3]);
    
    // Posición final
    gl_Position = projection_mat * inverse(view_mat) * model_mat * vec4(position, 1.0);
    
    // Pass-through
    color = vertex_color;
    UV = vertex_uv;
}