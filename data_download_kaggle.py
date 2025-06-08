import os
import shutil
import kagglehub

# Ruta base del proyecto
project_root = os.path.dirname(os.path.abspath(__file__))

# Carpeta donde se moverán los archivos finales
final_data_dir = os.path.join(project_root, "data", "in")
os.makedirs(final_data_dir, exist_ok=True)

# Carpeta temporal de cache para kagglehub
kagglehub_cache = os.path.join(project_root, "temp_kagglehub")
os.environ["KAGGLEHUB_CACHE"] = kagglehub_cache

# Descargar el dataset
downloaded_path = kagglehub.dataset_download("jhonyjacobi/bank-attrition-detection")
print("Dataset descargado en:", downloaded_path)

# Copiar archivos planos al destino final
for filename in os.listdir(downloaded_path):
    full_path = os.path.join(downloaded_path, filename)
    if os.path.isfile(full_path):
        shutil.copy(full_path, final_data_dir)

print("Archivos copiados a:", final_data_dir)

# Eliminar toda la carpeta temporal de descarga de kagglehub
shutil.rmtree(kagglehub_cache)
print("Carpeta temporal eliminada:", kagglehub_cache)
