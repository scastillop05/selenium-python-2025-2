# Taller de automatización de pruebas con Selenium, Python, Cucumber, Gherkin, y el patrón Page Object Model (POM).

## Instalación de Herramientas

### Antes de iniciar, asegúrate de tener instaladas las siguientes herramientas:
    - Navegador Google Chrome (https://www.google.com/intl/es_us/chrome/)
	- Python (https://www.python.org/downloads/) 
	- Selenium (pip install selenium)
	- WebDriver para el navegador (Chrome o Firefox)
		- ChromeDriver (https://googlechromelabs.github.io/chrome-for-testing/#stable)
		- Asegurarse de que el archivo del WebDriver.exe esté en el PATH o en el mismo directorio del proyecto.
		- Behave para Cucumber con Python (pip install behave)
		- Cucumber para casos de prueba con Gherkin (Esto ya viene con Behave.)

### Para correr los tests, usa el comando:
	debes correrlo en la terminal o consola de comandos desde la raíz de tu proyecto.
	- behave features/login.feature 
	- behave features/shopping_cart.feature 

# 🧪 Pruebas Automatizadas con Behave (BDD)

Este proyecto utiliza **BDD (Behavior Driven Development)** con **Behave** para escribir pruebas legibles por humanos, utilizando **Gherkin** como lenguaje y **Selenium** para interactuar con la interfaz web. El diseño sigue el **Page Object Model (POM)**.

---

## 🚀 Pasos para crear una nueva prueba

### 1. Crear o identificar la funcionalidad a probar
Define qué funcionalidad vas a automatizar. Por ejemplo: login, agregar productos al carrito, filtrado de ítems, etc.

### 2. Crear o actualizar la clase de página (`.py`)
Usa el patrón **Page Object Model**. Crea una clase para la página web si no existe, y define los métodos necesarios.

```bash
project/
└── pages/
    ├── login_page.py
    ├── inventory_page.py
    └── base_page.py
```

### 3. Crear el archivo `.feature`
Escribe el escenario en lenguaje Gherkin. Usa `Feature`, `Scenario`, `Given`, `When`, `Then` y `And`.

```gherkin
Feature: Add to cart functionality

  Scenario: User adds a product to the cart
    Given I am logged in on the inventory page
    When I add the product "Sauce Labs Backpack" to the cart
    Then I should see 1 item in the cart
```

Guárdalo en la carpeta `features/`.

### 4. Crear el archivo de `steps`
Aquí implementas en Python lo que hacen los pasos del `.feature`. Usa las clases del POM para interactuar con la UI.

```bash
project/
└── features/
    ├── steps/
    │   └── cart_steps.py
    └── shopping_cart.feature
```

Ejemplo de step:

```python
@when('I add the product "{product_name}" to the cart')
def step_impl(context, product_name):
    context.inventory_page.add_product_to_cart(product_name)
```

### 5. Ejecutar las pruebas

En la terminal, dentro del proyecto, ejecuta:

```bash
behave
```

También puedes correr un archivo específico:

```bash
behave features/shopping_cart.feature
```

---

# 🧑‍🏫 Ejercicios para el Taller de Pruebas Automatizadas con Selenium

A continuación se presentan dos ejercicios prácticos que los estudiantes deberán realizar durante el taller. Estos están diseñados para reforzar conceptos clave como la interacción con elementos web, localización por selectores y verificación de resultados.

---
## 🧪 Ejercicio 1: Buscar una película en IMDb y validar su calificación
### 💡 Sitio:
https://www.imdb.com

### 🎯 Escenario:
Buscar la película “Inception”, abrir el primer resultado y verificar que en la página se muestre correctamente el título y la calificación (rating).

### ✅ Requisitos que practican:
- Interacción con un campo de búsqueda real
- Navegación entre resultados
- Uso de diferentes tipos de selectores (ID, XPATH, CSS)
- Validación de texto y valores numéricos
- Estructuración básica de un flujo de prueba

## 🧪 Ejercicio 2: Buscar un producto en MercadoLibre y validar su precio
### 💡 Sitio:
https://www.mercadolibre.com.co

### 🎯 Escenario:
Buscar “audífonos”, seleccionar el primer resultado y validar que en la página del producto se muestra un título y un precio válidos.

### ✅ Requisitos que practican:
- Automatización de una búsqueda en una web real
- Navegación hacia un resultado específico
- Uso de selectores por nombre, clase o XPATH
- Validación de texto y presencia de elementos
- Comprensión de flujo completo: búsqueda → selección → validación