# Crosshair Overlay - v1

Este proyecto proporciona un overlay de crosshair en el centro de la pantalla utilizando `tkinter` y `PIL` (Python Imaging Library). Es totalmente funcional siempre cuando tengas instalado todos los requisitos.

## Requisitos

- Python 3.x
- `tkinter` (generalmente incluido con Python)
- `Pillow` (PIL)
- `ctypes` (incluido con Python)

## Uso

1. **Coloca tu imagen de crosshair** en el mismo directorio que `crosshair_overlay_v1.py`. Asegúrate de que la imagen se llame `Crosshair.png` o actualiza la variable en la linea 30 `image_path` en el script con el nombre de tu imagen.

2. **Ejecuta el script**:
   - Abre una terminal (ctrl + ñ).
   - Ejecuta el script:
     ```sh
     python crosshair_overlay_v1.py
     ```

3. **Inicia tu juego** en modo ventana sin bordes o ventana completa para asegurarte de que el overlay del crosshair se mantenga visible.

4. **Para cerrar el overlay**, presiona la tecla `Esc` o cierre el manualmente.

### Notas:
- Asegúrate de que la ventana del juego no esté en modo pantalla completa exclusiva, ya que esto podría ocultar la ventana del crosshair.
- Si encuentras problemas con la superposición, puedes ajustar la configuración de la ventana del juego o usar software de terceros para mantener la ventana del crosshair siempre en primer plano.