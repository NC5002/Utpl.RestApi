# Utpl.RestApi

Proyecto para trabajar con APIs en REST utilizando FastAPI.  
The project will work with REST APIs using FastAPI.

---

## Descripción del Proyecto / Project Description

Este proyecto es una aplicación web construida utilizando **FastAPI**, un framework moderno, rápido y fácil de usar para crear APIs en Python. Es ideal para construir aplicaciones backend eficientes y escalables.  
This project is a web application built using **FastAPI**, a modern, fast, and easy-to-use Python framework for creating APIs. It is ideal for building efficient and scalable backend applications.

### Caso de Estudio: API de Gestión para "Come en Casa"  
**Case Study: Management API for "Come en Casa"**

**Objetivos / Objectives:**
- Gestionar el catálogo de almuerzos.  
  Manage the lunch catalog.
- Modernizar el sistema de gestión de pedidos y clientes.  
  Modernize the order and customer management system.
- Proporcionar una base para futuras integraciones con sistemas de pago y notificaciones automáticas.  
  Provide a foundation for future integrations with payment systems and automatic notifications.

**Descripción / Description:**  
"Come en Casa" busca modernizar su sistema de gestión, pasando de un proceso manual a un API eficiente que permita manejar clientes, pedidos y un catálogo de almuerzos. Este proyecto tiene como objetivo construir un API robusta y escalable para satisfacer estas necesidades.  
"Come en Casa" aims to modernize its management system, transitioning from a manual process to an efficient API that can handle customers, orders, and a lunch catalog. This project aims to build a robust and scalable API to meet these needs.

**Más Información / More Information:**  
[Case Study - Come en Casa](https://gamma.app/docs/Caso-de-Estudio-API-de-Gestion-para-Come-en-Casa-326k6uflo3hrek4)

**Despliegue en Render / Deployment on Render:**  
[Utpl.RestApi on Render](https://utpl-restapi-k6j7.onrender.com)

---

## Requisitos / Requirements

### Dependencias / Dependencies

Asegúrate de tener instaladas las siguientes dependencias:  
Make sure you have the following dependencies installed:

- **Python 3.6 o superior / Python 3.6 or higher**: [Descargar Python / Download Python](https://www.python.org/downloads/)
- **FastAPI**: Instala FastAPI y Uvicorn (servidor ASGI) usando pip:  
  Install FastAPI and Uvicorn (ASGI server) using pip:
  ```bash
  pip install fastapi uvicorn
  ```
- **Otras dependencias / Other dependencies**: Todas las dependencias necesarias están listadas en el archivo `requirements.txt`. Puedes instalarlas ejecutando:  
  All required dependencies are listed in the `requirements.txt` file. You can install them by running:
  ```bash
  pip install -r requirements.txt
  ```

---

## Instalación y Configuración / Installation and Configuration

Sigue estos pasos para configurar y ejecutar el proyecto localmente:  
Follow these steps to set up and run the project locally:

1. **Clona el repositorio / Clone the repository:**
   ```bash
   git clone https://github.com/tu-usuario/Utpl.RestApi.git
   cd Utpl.RestApi
   ```

2. **Crea un entorno virtual (opcional pero recomendado) / Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate / On Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias / Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta la aplicación / Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Accede a la API / Access the API:**
   - **Local:** Abre tu navegador y visita [http://127.0.0.1:8000](http://127.0.0.1:8000).  
     Open your browser and visit [http://127.0.0.1:8000](http://127.0.0.1:8000).
   - **Documentación interactiva / Interactive documentation:** Accede a la documentación de la API en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) o [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).  
     Access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) or [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

---
## Documentación del Proceso de Desarrollo / Development Process Documentation

### Configuración del Workflow / Workflow Configuration
- Se utilizó **Git** para el control de versiones y **GitHub** para la gestión del repositorio.  
  **Git** was used for version control and **GitHub** for repository management.
- Se implementó un flujo de trabajo basado en ramas (`feature branches`) para el desarrollo de nuevas funcionalidades.  
  A branch-based workflow (`feature branches`) was implemented for developing new features.

### Decisiones Técnicas / Technical Decisions
- **FastAPI** fue elegido por su rendimiento, facilidad de uso y soporte nativo para validación de datos y documentación automática.  
  **FastAPI** was chosen for its performance, ease of use, and native support for data validation and automatic documentation.
- **SQLModel** se utilizó para la gestión de la base de datos, combinando la simplicidad de Pydantic con la potencia de SQLAlchemy.  
  **SQLModel** was used for database management, combining the simplicity of Pydantic with the power of SQLAlchemy.

### Desafíos y Soluciones / Challenges and Solutions
- **Desafío:** Integración de relaciones complejas entre modelos.  
  **Challenge:** Integration of complex relationships between models.
  **Solución:** Se utilizó SQLModel para definir relaciones y back-populates en los modelos.  
  **Solution:** SQLModel was used to define relationships and back-populates in the models.

---

## Pruebas / Testing

Se realizaron pruebas unitarias y de integración para garantizar el correcto funcionamiento de la API.  
Unit and integration tests were conducted to ensure the proper functioning of the API.

### Ejecución de Pruebas / Running Tests
Para ejecutar las pruebas, utiliza el siguiente comando:  
To run the tests, use the following command:
```bash
pytest
```

---

## Contribuciones / Contributions

¡Las contribuciones son bienvenidas! Si deseas contribuir al proyecto, sigue estos pasos:  
Contributions are welcome! If you wish to contribute to the project, follow these steps:

1. Haz un fork del repositorio.  
   Fork the repository.
2. Crea una rama para tu feature o corrección: `git checkout -b feature/nueva-funcionalidad`.  
   Create a branch for your feature or fix: `git checkout -b feature/new-feature`.
3. Realiza tus cambios y haz commit: `git commit -m 'Añadir nueva funcionalidad'`.  
   Make your changes and commit: `git commit -m 'Add new feature'`.
4. Sube tus cambios: `git push origin feature/nueva-funcionalidad`.  
   Push your changes: `git push origin feature/new-feature`.
5. Abre un Pull Request.  
   Open a Pull Request.

---
## Contacto / Contact

Si tienes alguna pregunta o sugerencia, no dudes en contactarme:  
If you have any questions or suggestions, feel free to contact me:

- **Nombre / Name:** Nicole Calvas
- **Email:** ncwork.350@outlook.com
- **GitHub:** https://github.com/NC5002
😊
