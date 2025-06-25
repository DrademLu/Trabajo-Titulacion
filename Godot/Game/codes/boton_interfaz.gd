# UI.gd
extends Control

@onready var btn_cliente  = $HBoxContainer/BotonCliente
@onready var btn_servidor = $HBoxContainer/BotonServidor
@onready var btn_historic = $HBoxContainer/BotonHistoricos

func _ready() -> void:
	btn_cliente.pressed.connect(Callable(self, "_on_btn_cliente_pressed"))
	btn_servidor.pressed.connect(Callable(self, "_on_btn_servidor_pressed"))
	btn_historic.pressed.connect(Callable(self, "_on_btn_historic_pressed"))

func _on_btn_cliente_pressed() -> void:
	get_tree().change_scene_to_file("res://scenes/cliente_main.tscn")

func _on_btn_servidor_pressed() -> void:
	get_tree().change_scene_to_file("res://scenes/server_main.tscn")

func _on_btn_historic_pressed() -> void:
	var path := "C:/LogsGodot"
	# Normalizar la ruta para Windows
	path = path.replace("/", "\\")
	print("[DEBUG] Intentando abrir carpeta: %s" % path)
	# Verificar si la carpeta existe
	var dir := DirAccess.open(path)
	if dir:
		print("[DEBUG] Carpeta encontrada, abriendo en explorador")
		var error := OS.shell_open(path)
		if error != OK:
			push_error("Error al abrir la carpeta: %d" % error)
	else:
		push_error("Carpeta no encontrada: %s" % path)
