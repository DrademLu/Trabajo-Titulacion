LIBNAME       = probando

# Archivos fuente
LIB_SOURCES   = src/escritor.c \
                src/opcua_connecion.c \
                src/opcua_tomar.c \
                src/opcua_suscripcion.c \
                src/opcua_server.c
APP_SOURCES   = test/main.c

# Compilador y flags
CC            = x86_64-w64-mingw32-gcc
CFLAGS        = -Wall -fPIC -Iinclude -I/mingw64/include -DBUILD_DLL -g
LDFLAGS       = -L$(LIB_DIR)
LDFLAGS_SHARED= -shared -Wl,--out-implib,$(LIB_DIR)/lib$(LIBNAME).a
LDLIBS        = -lopen62541
APPLDLIBS     = -l$(LIBNAME) -lopen62541

RM            = rm -rf

# Detectar plataforma
ifeq ($(OS),Windows_NT)
    EXE_EXT     = .exe
    SHARED_EXT  = .dll
    BUILD_DIR   = build_win64
    DEFINES     = -DBUILD_DLL
else
    EXE_EXT     =
    SHARED_EXT  = .so
    BUILD_DIR   = build_linux
    DEFINES     =
    APPLDLIBS   += -Wl,-rpath,'$$ORIGIN'
endif

# Directorios de salida
LIB_DIR       = $(BUILD_DIR)/lib
OBJ_DIR       = $(BUILD_DIR)/obj
BIN_DIR       = $(BUILD_DIR)/bin

# Objetos
LIB_OBJECTS   = $(patsubst src/%.c,$(OBJ_DIR)/src/%.o,$(LIB_SOURCES))
APP_OBJECTS   = $(patsubst test/%.c,$(OBJ_DIR)/test/%.o,$(APP_SOURCES))

# Targets
.PHONY: all clean dirs

all: dirs \
	$(LIB_DIR)/lib$(LIBNAME)$(SHARED_EXT) \
	$(BIN_DIR)/app$(EXE_EXT)

dirs:
	mkdir -p $(OBJ_DIR)/src $(OBJ_DIR)/test $(LIB_DIR) $(BIN_DIR)

# Compila cada .c a objeto
$(OBJ_DIR)/src/%.o: src/%.c
	$(CC) $(CFLAGS) $(DEFINES) -c $< -o $@

$(OBJ_DIR)/test/%.o: test/%.c
	$(CC) $(CFLAGS) -c $< -o $@

# Crear la librería compartida + import-lib
$(LIB_DIR)/lib$(LIBNAME)$(SHARED_EXT): $(LIB_OBJECTS)
	$(CC) $(LDFLAGS_SHARED) $(CFLAGS) -o $@ $^ $(LDFLAGS) $(LDLIBS)

# Crear el ejecutable que usa la librería compartida
$(BIN_DIR)/app$(EXE_EXT): $(APP_OBJECTS) | $(LIB_DIR)/lib$(LIBNAME)$(SHARED_EXT)
	$(CC) $(CFLAGS) -o $@ $^ -L$(LIB_DIR) $(APPLDLIBS)

clean:
	-$(RM) $(OBJ_DIR)
	-$(RM) $(LIB_DIR)/*$(SHARED_EXT) $(LIB_DIR)/lib$(LIBNAME).a
	-$(RM) $(BIN_DIR)/*$(EXE_EXT)