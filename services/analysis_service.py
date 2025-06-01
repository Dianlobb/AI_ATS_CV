import time
from services.openai_service import create_thread_and_run, wait_on_run, get_response, upload_file_to_assistant




def process_resume(upload_file, job_role, job_description):
    # Validar y subir archivo
    file_obj = upload_file_to_assistant(upload_file)
    analysis_message = build_analysis_message(upload_file.name, job_role, job_description)
    thread, run = create_thread_and_run(analysis_message, file_obj.id)
    run = wait_on_run(run, thread)
    response = get_response(thread)
    
    return response


def build_analysis_message(filename, job_role, job_description):
    msg = f"analizar este CV '{filename}' para compatibilidad ATS y matching con rol."
    if job_role:
        msg += f" para el puesto: {job_role}"
    if job_description:
        msg += f"\nDescripción del trabajo:\n{job_description}"
    msg += "\nIncluye análisis: 1. Puntuación ATS, 2. Detección de habilidades, 3. Match del trabajo, 4. Revisión de formato, 5. Optimización de palabras clave, 6. Recomendaciones."
    return msg