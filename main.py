# Crea Generador de Contraseñas Profesional Flet.
import flet as ft
import random # nos da caracteres al azar.
import string # para trabajar con caracteres.

# Función principal
def main(page: ft.Page):
    page.window.icon = "assets/icon.ico"    
    page.title = "WORD WAT SOLUTIONS - Create Keys"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Agregamos la imagen GIF al título
    titulo_imagen = ft.Image(
        src="assets/terre-19.gif",
        width=50,
        height=50,
        fit=ft.ImageFit.CONTAIN
    )
    
    titulo_texto = ft.Text(
        "WORD WAT SOLUTIONS\nGENERADOR DE CONTRASEÑAS",
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.CENTER
    )
    # Change Row to Column for vertical stacking
    titulo_container = ft.Column(
        [titulo_imagen, titulo_texto],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )
    
    # Creamos un contenedor para el título con la imagen
    titulo_container = ft.Row(
        [titulo_imagen, titulo_texto],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )
    
    # Crear una referencia al texto de longitud
    length_text = ft.Text(
        value="12",  # valor inicial
        size=20,
        text_align=ft.TextAlign.CENTER
    )

    # Función generar password.
    def generate_password(length, use_uppercase, use_numbers, use_symbols):
        characters = string.ascii_letters
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))
    
    # Función actualizar contraseña.
    def update_password(e):
        # Actualizar el texto de longitud
        length_text.value = str(int(length_slider.value))
        password_field.value = generate_password(
            int(length_slider.value),
            uppercase_switch.value,
            numbers_switch.value,
            symbols_switch.value
        )
        page.update()

    # Función portapapeles.
    def copy_to_clipboard(e):
        page.set_clipboard(password_field.value)
        snack_bar = ft.SnackBar(ft.Text("Contraseña copiada al portapapeles"))
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()

    # Cuadro de texto solo lectura.
    password_field = ft.TextField(
        read_only=True,
        width=600,
        text_align=ft.TextAlign.CENTER,
        text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD)
    )

    # Creamos el slider para el tamaño de la contraseña, minimo=8, maximo=128, por definición=12.
    length_slider = ft.Slider(min=8, max=128, divisions=24, label="{value}",
                            value=12, on_change=update_password)

    # Creamos el boton que genera la contraseña.
    generate_button = ft.ElevatedButton("Generar contraseña", on_click=update_password,
                                        icon=ft.icons.REFRESH)
    # Botones para elegir tipo contraseña.
    uppercase_switch = ft.Switch(label="Incluir Mayúsculas", value=True, on_change=update_password)
    numbers_switch = ft.Switch(label="Incluir Números", value=True, on_change=update_password)
    symbols_switch = ft.Switch(label="Incluir Símbolos", value=True, on_change=update_password)

    # Creamos boton de copiar al portapapeles.
    copy_button = ft.ElevatedButton(
        "Copiar al portapapeles",
        on_click=copy_to_clipboard,
        icon=ft.icons.COPY
    )

    page.add(
        titulo_container,
        ft.Column(
            [
                ft.Text("Longitud Contraseña"),
                length_text,  # Usar la referencia creada
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        length_slider,
        uppercase_switch, 
        numbers_switch,
        symbols_switch,
        password_field,
        ft.Row(
            [generate_button, copy_button],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )
    )
    
ft.app(target=main, assets_dir="assets")