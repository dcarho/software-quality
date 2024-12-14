#!/bin/bash

# Ruta al directorio de tests
TEST_DIR="test"

# Ejecuta los tests con unittest
echo "Ejecutando tests en la carpeta '$TEST_DIR'..."
python3 -m unittest discover -s "$TEST_DIR"

# Verifica si los tests pasaron
if [ $? -ne 0 ]; then
    echo "❌ Tests fallaron. Cancela el commit."
    exit 1
else
    echo "✅ Todos los tests pasaron. Procediendo con el commit."
fi
