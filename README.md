# Instrucciones para correr los archivos del proyecto
#
## Requisitos
- Python 3
- Visual Studio Code
- Extensión [PlantUML](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml)
- [Graphviz](https://graphviz.gitlab.io/download/) (necesario para renderizar diagramas UML)

## Visualizar el diagrama UML (`modelo.puml`)

1. Instala la extensión de PlantUML en VS Code (recomendada) o asegúrate de tener PlantUML y Graphviz
2. Abre el archivo `modelo.puml` en VS Code.
3. Haz clic derecho en el editor y selecciona "Preview Current Diagram" o usa el atajo `Alt+D` para ver el diagrama.

### Solución de problemas
- Si no ves el diagrama, verifica que la extensión PlantUML esté instalada y Graphviz esté correctamente configurado en tu sistema.
- Revisa que el archivo `modelo.puml` no tenga errores de sintaxis.
- Como ultimo recurso puedes copiar y pegar el código en PlantUML en la web y el diagrama se verá correctamente.


## Ejecutar el archivo principal (`main.py`)

1. Asegúrate de tener Python 3 instalado.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el archivo con:
   ```powershell
   python main.py
   ```

Si tienes problemas, asegúrate de estar en la carpeta correcta y que Python esté en tu PATH.
