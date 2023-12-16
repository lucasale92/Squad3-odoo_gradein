[![](https://github.com/lucasale92/Squad3-odoo_gradein/blob/main/Readm2.jpg?raw=true)](https://github.com/lucasale92/Squad3-odoo_gradein/blob/main/Readm2.jpg?raw=true)

<h1> Proyecto Squad3-odoo-gradein</h1>
<h2>1. Introducción</h2>

En este proyecto se desarrolla una interfaz "Menu services" para poder facilitar a los usuarios una estrategia de "canje”, donde los mismos puedan entregar equipos usados (móviles u otros), como parte de pago en la adquisición de nuevos productos, en tiendas físicas.


<h2>2. Objetivo </h2>🎯

Creación de módulos en Odoo que permita configurar la condición de GradeIn (determinación del precio del equipo usado en base a la condición en la que se encuentra) en el sistema central, habilitando así a todas las tiendas físicas de la empresa su uso y puesta en marcha.


<h2>3. Software</h2> 💻

✔ IDE (VSCode o Pycharm).</br>
✔ Instalación de ultima version de Python disponible.</br>
✔ Instalación de ultima version de Git disponible.</br>
✔ Docker desktop, para creacion de contenedores.</br>
✔ Jira.</br>
✔ Utilización del ORM de Odoo.

<h2>4. Instalación</h2>

1. Realizar instalacion del Docker Desktop
	https://www.docker.com/get-started/
2. Creacion de contenedores 
		PostgreSQL + Odoo. Creacion y seteo del contenedor archivo .yml
3. Clonar Repositorio
		git clone https://github.com/lucasale92/Squad3-odoo_gradein.git
4. Ingresar al proyecto descargado y en la terminal levantar el contenedor
``  docker compose up    ``
5. Loguearse en la interfaz del Odoo
![](https://github.com/lucasale92/Squad3-odoo_gradein/blob/main/Interfaz.JPG?raw=true)

6. Instalar el modulo # Squad3-odoo_gradein: 
![](https://github.com/lucasale92/Squad3-odoo_gradein/blob/main/Interfaz2.JPG?raw=true)

7. El modulo instalado tendra dos tipos de acceso:
	+ Administrator: tiene acceso al Gradein Order y a la configuracion
![](https://github.com/lucasale92/Squad3-odoo_gradein/blob/main/Interfaz_admin.jpg?raw=true)
	+ Seller: el vendedor solo tiene acceso al Gradein Order
![](https://github.com/lucasale92/Squad3-odoo_gradein/blob/main/Interfaz_seller.jpg?raw=true)

<h2>5. Descripción del proyecto</h2>

<h3>I. Modelos</h3>

**_init_.py **: organiza, importa y facilita el acceso a los módulos en el paquete gradein de la aplicación.

❇️**Modelo GradeIn_Answer:**

+ Propósito: Gestiona respuestas asociadas con evaluaciones o encuestas.
+ Campos:
	+ name: Nombre de la respuesta.
	+ active: Indica si la respuesta está activa.
	+ price_reduction: Representa la reducción de precio asociada.

❇️**Modelo GradeInEquipment:**

+ Propósito: Gestiona información sobre equipos.
+ Campos :
	+ name: Nombre del equipo.
	+ image: Imagen representativa del equipo.
	+ description: Descripción detallada del equipo.
	+ active: Indica si el equipo está activo.
	+ price: Precio asociado con el equipo.

❇️**Modelo GradeIn_Equipment_Type:**

+ Propósito: Clasifica y organiza diferentes tipos de equipos.
+ Campos:
	+ name: Nombre del tipo de equipo.
	+ image: Imagen representativa del tipo de equipo.
	+ active: Indica si el tipo de equipo está activo.
	+ question_ids: Relación con preguntas asociadas.

❇️**Modelo GradeIn_Order:**

+ Propósito: Gestiona órdenes o transacciones.
+ Campos:
	+ name: Nombre de la orden.
	+ date: Fecha de la orden.
	+ state: Estado de la orden (borrador, confirmada, rechazada).
	+ equipment_id: Equipo asociado a la orden.
	+ imei: IMEI asociado a la orden.
	+ partner_id: Cliente o socio asociado a la orden.
	+ price: Precio de la orden.
	+ review: Comentarios o revisiones asociadas.
	+ answer_ids: Relación con respuestas asociadas.
	+ question_id: Pregunta asociada.
	+ reject_motive_id: Motivo de rechazo asociado.
	+ image_ids: Imágenes asociadas a la orden.

❇️**Modelo GradeInQuestion:**

+ Propósito: Define preguntas para evaluaciones o encuestas.
+ Campos:
	+ name: Nombre de la pregunta.
	+ active: Indica si la pregunta está activa.
	+ equipment_type_ids: Relación con tipos de equipos asociados.
	+ answer_ids: Relación con respuestas asociadas.

❇️**Modelo GradeInRejectMotive:**

+ Propósito: Define motivos de rechazo.
+ Campos:
	+ name: Nombre del motivo de rechazo.
	+ active: Indica si el motivo de rechazo está activo.

<h3>II. Reporte</h3>

❇️**Modelo Abstracto GradeinReport (gradein_reports.py)**
+ Propósito: Diseñado para la generación de informes relacionados con órdenes.
+ Funcionalidad Clave: Método _get_report_values: Recopila datos necesarios para la generación del informe.

❇️**Plantilla de Informe (gradein_order_report.xml ):**
+ Estructura: Utiliza el formato QWeb para definir la estructura del informe.
+ Contenido: Muestra detalles específicos de las órdenes en una tabla, incluyendo nombre, fecha, ID de equipo, IMEI, imágenes, ID de socio, motivo de rechazo, precio y revisión.
+ Funciones:
	+ Registro de Acción de Informe (action_gradein_order_report): Registra una acción de informe en Odoo.
	+ Vincula el informe al modelo gradein.order.
	+ Especifica el tipo de informe como QWeb-PDF.

### III. Icono del modulo
	**icon.png:**
- Ubicación: static/description/icon.png
- Propósito: Representa el ícono asociado con la descripción del módulo, en este caso una mano con un celular.

<h3>IV. Vistas</h3>
</br>

⏺️**Vista de Respuestas (view_gradein_answer_form)**

- <u> Formulario (view_gradein_answer_form)</u>: Define la estructura del formulario para el modelo gradein.answer. Incluye campos como name, active, y price_reduction en un grupo.

- <u>Tree (view_gradein_answer_tree)</u>: Define la estructura de la vista de árbol para el modelo gradein.answer. Muestra campos como name y price_reduction en formato de lista.

- <u>Búsqueda (view_gradein_answer_search)</u>: Define la estructura de la vista de búsqueda para el modelo gradein.answer. Incluye: 
	- Un campo para filtrar por name.
	- Incluye un filtro para elementos no activos (active_filter).

- <u>Acción de Ventana (action_gradein_answers)</u>: Define una acción de ventana para el modelo gradein.answer. 
	- Especifica las vistas que deben mostrarse: tree, form, y search.
	- Utiliza la vista de árbol (view_gradein_answer_tree) como vista predeterminada.
	- Accesible a través del elemento de menú "Answer".
</br>

⏺️**Vista de Tipo de Equipo (view_gradein_equipment_type_form)**

- <u>Formulario (view_gradein_equipment_type_form)</u>: Define la estructura del formulario para el modelo gradein.equipment.type.
	- Incluye campos como name, active, image, y question_ids en un grupo.
 
 - <u>Árbol (view_gradein_equipment_type_tree)</u>: Define la estructura de la vista de árbol para el modelo gradein.equipment.type.
	- Muestra el campo name en formato de lista.

- <u>Búsqueda (view_gradein_equipment_type_search)</u>: Define la estructura de la vista de búsqueda para el modelo gradein.equipment.type. Incluye:
	- Campo para filtrar por name.
	- Filtro para elementos no activos (active_filter).

- <u>Acción de Ventana (action_gradein_equipments_type)</u>: Define una acción de ventana para el modelo gradein.equipment.type.
-	Especifica las vistas que deben mostrarse: tree, form, y search.
-	Utiliza la vista de árbol (view_gradein_equipment_type_tree) como vista predeterminada.
-	Accesible a través del elemento de menú "Equipment Type" en el menú de configuración.
</br>

⏺️**Vista de Equipo (view_gradein_equipment_form)**

- <u>Formulario (view_gradein_equipment_form)</u>:Define la estructura del formulario para el modelo gradein.equipment.
	-Incluye campos como name, image, description, active, y price en un grupo.

- <u>Árbol (view_gradein_equipment_tree):</u>Define la estructura de la vista de árbol para el modelo gradein.equipment.
	- Muestra campos como name, description, y price en formato de lista.

- <u>Búsqueda (view_gradein_equipment_search)</u>: Define la estructura de la vista de búsqueda para el modelo gradein.equipment.
	- Incluye campos para filtrar por name y description.
	- Incluye un filtro para elementos activos.

- <u>Acción de Ventana (action_gradein_equipment)</u>: Define una acción de ventana para el modelo gradein.equipment.
	- Especifica las vistas que deben mostrarse: tree, form, y search.
	- Utiliza la vista de árbol (view_gradein_equipment_tree) como vista predeterminada.
	- Accesible a través del elemento de menú "Equipment" en el menú de servicios.

</br>
    
 ⏺️⏺️  **Vista de Orden GradeIn: (view_gradein_order_form)**

- <u>Formulario (view_gradein_order_form)</u>: Define la estructura del formulario para el modelo gradein.order.
	- Incluye campos como name, date, state, equipment_id, imei, image_ids, partner_id, reject_motive_id, price, review, answer_ids, y question_id en un grupo.

- <u>Árbol (view_gradein_order_tree)</u>: Define la estructura de la vista de árbol para el modelo gradein.order.
	- Muestra campos como name, date, state, equipment_id, imei, partner_id, reject_motive_id, y price en formato de lista.

- <u>Búsqueda (view_gradein_order_search):</u>Define la estructura de la vista de búsqueda para el modelo gradein.order.
	-Incluye campos como name, date, imei, equipment_id, y reject_motive_id.
	-Incluye un filtro para elementos en estado "Draft".

- <u>Acción de Ventana (action_gradein_order)</u>:Define una acción de ventana para el modelo gradein.order.
	- Especifica las vistas que deben mostrarse: tree, form, y search.
	- Utiliza la vista de árbol (view_gradein_order_tree) como vista predeterminada.
	- Accesible a través del elemento de menú "Order GradeIn" en el menú de servicios.
</br>

⏺️**Vista de Preguntas (view_gradein_question_form)**

- <u>Formulario (view_gradein_question_form)</u>:Define la estructura del formulario para el modelo gradein.question.
	- Incluye campos como name, active, equipment_type_ids, y answer_ids en un grupo.

- <u>Árbol (view_gradein_question_tree)</u>: Define la estructura de la vista de árbol para el modelo gradein.question.
	- Muestra campos como name, active, y equipment_type_ids en formato de lista.

- <u>Búsqueda (view_gradein_question_search)</u>: Define la estructura de la vista de búsqueda para el modelo gradein.question.
	- Incluye un campo para filtrar por name.
	- Incluye un filtro para elementos activos.

- <u>Acción de Ventana (action_gradein_questions)</u>:Define una acción de ventana para el modelo gradein.question.
	- Especifica las vistas que deben mostrarse: tree, form, y search.
	- Utiliza la vista de árbol (view_gradein_question_tree) como vista predeterminada.
	 - Accesible a través del elemento de menú "Questions" en el menú de servicios.
</br>

⏺️**Vista de Motivo de Rechazo (view_gradein_reject_motive_form)**
- <u>Formulario (view_gradein_reject_motive_form)</u>: Define la estructura del formulario para el modelo gradein.reject.motive.
	- Incluye campos como name y active en un grupo.

- <u>Árbol (view_gradein_reject_motive_tree)</u>: Define la estructura de la vista de árbol para el modelo gradein.reject.motive.
	- Muestra campos como name y active en formato de lista.

- <u>Búsqueda (view_gradein_answer_search)</u>: Define la estructura de la vista de búsqueda para el modelo gradein.reject.motive.
	- Incluye un campo para filtrar por name.
	- Incluye un filtro para elementos no activos.

- <u>Acción de Ventana (action_gradein_reject_motive)</u>: Define una acción de ventana para el modelo gradein.reject.motive.
	- Especifica las vistas que deben mostrarse: tree, form, y search.
	- Utiliza la vista de árbol (view_gradein_reject_motive_tree) como vista predeterminada.
	 -Accesible a través del elemento de menú "Reject Motive" en el menú de configuración.

<h3>V. Archivos de configuracion: _init_.py y manifest.py</h3>

**_init_.py** importa tres partes fundamentales del mismo paquete:
	- models: Define modelos de datos.
	- reports: Incluye lógica relacionada con informes.
	- static: Contiene archivos estáticos como imágenes y scripts.

**manifest.py**: es un archivo de descripción del módulo (addon) . 
A continuación, se explica la funcionalidad de cada campo: </br>
	- name: Nombre del módulo. Identifica el módulo de manera única en el sistema

	- version: Versión del módulo. Indica la versión actual del módulo.

    - author: Autor o autores del módulo. Proporciona información sobre quién desarrolló el módulo.

    - depends: Dependencias del módulo. Especifica otros módulos de Odoo que deben estar instalados para que este módulo funcione 
    correctamente.
    - installable: Indica si el módulo se puede instalar. Determina si el módulo es instalable desde la interfaz de administración.

    - application: Indica si el módulo es una aplicación. Si es True, indica que el módulo es una aplicación funcional en lugar de una biblioteca o un tema.

    - data: Lista de archivos XML y archivos de datos para cargar. Especifica los archivos XML y de datos que Odoo debe cargar durante la instalación.

    - images: Lista de imágenes relacionadas con el módulo. Incluye imágenes que se mostrarán en la interfaz de Odoo, por ejemplo, el icono del módulo.
    
</br>
<h3> VI. GIT IGNORE</h3>
**.gitignore** es un archivo de configuración utilizado por el sistema de control de versiones Git. Su propósito principal es indicar a Git qué archivos o directorios debe ignorar y no incluir en el seguimiento o control de versiones


<h2>6. Estructura del Proyecto</h2>
Squad3-odoo_gradein/</br>
├── models/</br>
│   ├── _init_.py</br>
│   ├── gradein_answer.py</br>
│   ├── gradein_equipment.py</br>
│   ├── gradein_equipment_type.py</br>
│   ├── gradein_order.py</br>
│   ├── gradein_question.py</br>
│   ├── gradein_reject_motive.py</br>
│   └── menu.py</br>
├── reports/</br>
│   ├── _init_.py</br>
│   ├── gradein_reports.py</br>
│   └── gradein_reports.xml</br>
├── security/</br>
│   ├── ir.model.access.csv</br>
│   └── res_groups.xml</br>
├── static/</br>
│   └── description/</br>
│       └── icon.png</br>
├── views/</br>
│   ├── gradein_answer_views.xml</br>
│   ├── gradein_equipment_type_views.xml</br>
│   ├── gradein_equipment_views.xml</br>
│   ├── gradein_order_views.xml</br>
│   ├── gradein_question_views.xml</br>
│   └── gradein_rejection_motive.xml</br>
│       └── menu_services.xml</br>
├── .gitignore</br>
├── README.md</br>
├── Readm2.jpg</br>
├── _init_.py</br>
└── _manifest_.py

