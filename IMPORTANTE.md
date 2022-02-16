Para permitir que Tesseract reconozca otros lenguajes, sigue estos pasos (solo funcionan para macOS/Ubuntu)

1. Clona el repositorio **tessdata**, así (tardará un rato porque pesa casi 5GB):

```
git clone https://github.com/tesseract-ocr/tessdata
```

2. Muévete al directorio: 

```
cd tessdata
```

3. Obtén la ruta completa usando **pwd**:

```
pwd 
```

4. Toma el resultado del paso anterior y añádelo a la variable de entorno **TESSDATA_PREFIX**:

```
export TESSDATA_PREFIX=/home/jesus/DataSmarts/tessdata
```