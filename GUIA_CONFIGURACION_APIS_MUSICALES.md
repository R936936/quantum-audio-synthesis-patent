# 🎵 GUÍA DE CONFIGURACIÓN DE APIS MUSICALES

## Configuración Profesional para Datos Reales

Esta guía te ayudará a configurar las credenciales necesarias para que el **AGENTECATALOGOSMUSICALES** obtenga datos 100% reales de plataformas de streaming y música.

---

## 📋 TABLA DE CONTENIDOS

1. [Spotify API](#1-spotify-api)
2. [YouTube Data API](#2-youtube-data-api)
3. [Last.fm API](#3-lastfm-api)
4. [MusicBrainz API](#4-musicbrainz-api)
5. [Instalación de Dependencias](#5-instalación-de-dependencias)
6. [Configuración Rápida](#6-configuración-rápida)
7. [Verificación](#7-verificación)

---

## 1. SPOTIFY API

### ¿Qué datos obtenemos?
- ✅ Popularidad de canciones (0-100)
- ✅ Audio features (danceability, energy, valence, etc.)
- ✅ Número de reproducciones estimado
- ✅ Artistas relacionados
- ✅ Géneros musicales
- ✅ Fecha de lanzamiento
- ✅ Duración de tracks

### Cómo obtener credenciales:

#### Paso 1: Crear cuenta de desarrollador
1. Ve a: **https://developer.spotify.com/dashboard**
2. Inicia sesión con tu cuenta de Spotify (o crea una gratis)
3. Acepta los términos de servicio

#### Paso 2: Crear una aplicación
1. Haz clic en **"Create app"**
2. Llena el formulario:
   - **App name**: `AgenteCatalogosMusicales`
   - **App description**: `Sistema de análisis de catálogos musicales`
   - **Website**: `http://localhost` (o tu sitio web)
   - **Redirect URI**: `http://localhost:8888/callback`
3. Marca las casillas de **"Web API"**
4. Haz clic en **"Save"**

#### Paso 3: Obtener credenciales
1. En el dashboard de tu app, haz clic en **"Settings"**
2. Copia el **Client ID** (visible directamente)
3. Haz clic en **"View client secret"** y copia el **Client Secret**
4. ⚠️ **IMPORTANTE**: Nunca compartas tu Client Secret públicamente

### Límites gratuitos:
- ✅ Sin costo
- ✅ Hasta 10,000 llamadas por día
- ✅ Suficiente para análisis profesionales

---

## 2. YOUTUBE DATA API

### ¿Qué datos obtenemos?
- ✅ Número de visualizaciones
- ✅ Likes y comentarios
- ✅ Fecha de publicación
- ✅ Engagement rate
- ✅ Tendencias de crecimiento
- ✅ Videos relacionados

### Cómo obtener credenciales:

#### Paso 1: Crear proyecto en Google Cloud
1. Ve a: **https://console.cloud.google.com/**
2. Inicia sesión con tu cuenta de Google
3. Haz clic en **"Select a project"** → **"New Project"**
4. Nombre del proyecto: `AgenteCatalogosMusicales`
5. Haz clic en **"Create"**

#### Paso 2: Habilitar YouTube Data API
1. En el menú, ve a **"APIs & Services"** → **"Library"**
2. Busca **"YouTube Data API v3"**
3. Haz clic en el resultado y luego en **"Enable"**

#### Paso 3: Crear credenciales
1. Ve a **"APIs & Services"** → **"Credentials"**
2. Haz clic en **"Create Credentials"** → **"API Key"**
3. Se creará una API Key automáticamente
4. (Opcional) Haz clic en **"Restrict Key"** para añadir seguridad:
   - **Application restrictions**: Ninguna (o IP addresses si sabes tu IP)
   - **API restrictions**: Selecciona **"YouTube Data API v3"**
5. Copia tu **API Key**

### Límites gratuitos:
- ✅ 10,000 unidades/día gratis
- ✅ 1 búsqueda = 100 unidades
- ✅ ~100 búsquedas por día

---

## 3. LAST.FM API

### ¿Qué datos obtenemos?
- ✅ Scrobbles (reproducciones totales)
- ✅ Listeners únicos
- ✅ Tendencias históricas
- ✅ Tags y géneros
- ✅ Artistas similares
- ✅ Top tracks por país

### Cómo obtener credenciales:

#### Paso 1: Crear cuenta de API
1. Ve a: **https://www.last.fm/api/account/create**
2. Inicia sesión con tu cuenta de Last.fm (o crea una gratis)

#### Paso 2: Crear aplicación
1. Llena el formulario:
   - **Application name**: `AgenteCatalogosMusicales`
   - **Application description**: `Sistema de análisis musical profesional`
   - **Application homepage**: `http://localhost`
   - **Callback URL**: `http://localhost:8888/callback`
2. Haz clic en **"Submit"**

#### Paso 3: Obtener credenciales
1. Te mostrarán tu **API Key** y **Shared Secret**
2. Copia ambos valores
3. El **API Key** es suficiente para lectura de datos
4. El **Shared Secret** solo se usa para funciones de escritura

### Límites gratuitos:
- ✅ Completamente gratis
- ✅ Sin límites de llamadas documentados
- ✅ Ideal para análisis históricos

---

## 4. MUSICBRAINZ API

### ¿Qué datos obtenemos?
- ✅ Metadata completa de artistas
- ✅ Discografía oficial
- ✅ Fechas de lanzamiento precisas
- ✅ Colaboraciones
- ✅ Información de sellos discográficos
- ✅ ISRCs y códigos de barras

### Cómo configurar:

#### No requiere API Key
MusicBrainz es completamente abierto y no requiere registro. Solo necesitas:

1. **Nombre de tu aplicación**: Ejemplo: `AgenteCatalogosMusicales/1.0`
2. **Email de contacto**: Tu email real para que puedan contactarte si hay problemas

### Límites:
- ✅ Completamente gratis
- ✅ 1 petición por segundo (rate limiting automático)
- ✅ Datos de alta calidad verificados por la comunidad

---

## 5. INSTALACIÓN DE DEPENDENCIAS

Antes de configurar, asegúrate de tener instaladas las librerías necesarias:

```bash
# Instalar dependencias para APIs
pip install spotipy requests python-dotenv musicbrainzngs

# O todas juntas
pip install spotipy requests python-dotenv musicbrainzngs youtube-dl pylast
```

### Descripción de librerías:
- **spotipy**: Cliente oficial de Spotify
- **requests**: Para llamadas HTTP a APIs
- **python-dotenv**: Manejo de variables de entorno
- **musicbrainzngs**: Cliente oficial de MusicBrainz
- **pylast**: Cliente de Last.fm
- **youtube-dl**: Extracción de datos de YouTube

---

## 6. CONFIGURACIÓN RÁPIDA

### Método Automático (Recomendado)

Ejecuta el configurador interactivo:

```bash
python3 ~/music_catalog_credentials_setup.py --setup
```

El asistente te guiará paso a paso para:
1. Ingresar tus credenciales de Spotify
2. Ingresar tu API Key de YouTube
3. Ingresar tu API Key de Last.fm
4. Configurar MusicBrainz
5. Guardar todo de forma segura

### Método Manual

Si prefieres configurar manualmente:

1. **Crear directorio de configuración**:
```bash
mkdir -p ~/.agente_catalogos_musicales
```

2. **Crear archivo de credenciales**:
```bash
nano ~/.agente_catalogos_musicales/.env
```

3. **Agregar tus credenciales**:
```bash
# Spotify API
SPOTIFY_CLIENT_ID=tu_client_id_aqui
SPOTIFY_CLIENT_SECRET=tu_client_secret_aqui

# YouTube Data API
YOUTUBE_API_KEY=tu_youtube_api_key_aqui

# Last.fm API
LASTFM_API_KEY=tu_lastfm_api_key_aqui
LASTFM_SHARED_SECRET=tu_lastfm_secret_aqui

# MusicBrainz API
MUSICBRAINZ_APP_NAME=AgenteCatalogosMusicales/1.0
MUSICBRAINZ_CONTACT=tu_email@example.com
```

4. **Proteger el archivo**:
```bash
chmod 600 ~/.agente_catalogos_musicales/.env
```

---

## 7. VERIFICACIÓN

### Verificar configuración

```bash
# Ver estado de configuración
python3 ~/music_catalog_credentials_setup.py --status
```

### Probar credenciales

```bash
# Probar conexión a todas las APIs
python3 ~/music_catalog_credentials_setup.py --test
```

Deberías ver:
```
✅ Spotify: Conexión exitosa
✅ YouTube: Conexión exitosa
✅ Last.fm: Conexión exitosa
✅ MusicBrainz: Conexión exitosa
```

---

## 🎯 CONFIGURACIÓN MÍNIMA RECOMENDADA

Para obtener datos completos y profesionales, se recomienda configurar al menos:

### Obligatorio:
- ✅ **Spotify API** - Datos de audio y popularidad más precisos

### Altamente Recomendado:
- ✅ **YouTube API** - Visualizaciones y engagement
- ✅ **MusicBrainz** - Metadata oficial (no requiere registro)

### Opcional:
- ⭐ **Last.fm** - Datos históricos y tendencias adicionales

---

## 🔒 SEGURIDAD

### Buenas prácticas:

1. **Nunca compartas tus credenciales**
   - No las subas a GitHub
   - No las envíes por email
   - No las pegues en chats públicos

2. **Protege tus archivos**
   ```bash
   chmod 600 ~/.agente_catalogos_musicales/.env
   chmod 600 ~/.agente_catalogos_musicales/credentials.json
   ```

3. **Regenera claves comprometidas**
   - Si accidentalmente expones una clave, regénérala inmediatamente
   - Spotify y YouTube permiten regenerar desde sus dashboards

4. **Usa variables de entorno**
   - El sistema carga automáticamente desde `.env`
   - Nunca hardcodees credenciales en código

---

## 🆘 SOLUCIÓN DE PROBLEMAS

### "Error 401: Unauthorized" en Spotify
- ✅ Verifica que el Client ID y Client Secret sean correctos
- ✅ Asegúrate de no tener espacios extra al copiar/pegar
- ✅ Regenera las credenciales en el dashboard de Spotify

### "Error 403: Forbidden" en YouTube
- ✅ Verifica que YouTube Data API v3 esté habilitada
- ✅ Asegúrate de que tu API Key no esté restringida incorrectamente
- ✅ Verifica tu cuota diaria (10,000 unidades)

### "Rate Limit Exceeded" en MusicBrainz
- ✅ MusicBrainz limita a 1 petición por segundo
- ✅ El sistema maneja esto automáticamente
- ✅ Si persiste, espera unos minutos

### "Invalid API Key" en Last.fm
- ✅ Verifica que copiaste la API Key completa
- ✅ Last.fm a veces tarda unos minutos en activar nuevas keys
- ✅ Intenta de nuevo después de 5 minutos

---

## 📞 SOPORTE

Si tienes problemas con la configuración:

1. **Verifica el estado**: `python3 ~/music_catalog_credentials_setup.py --status`
2. **Prueba las credenciales**: `python3 ~/music_catalog_credentials_setup.py --test`
3. **Revisa los logs**: El sistema mostrará errores específicos
4. **Consulta la documentación oficial** de cada API

---

## 🚀 PRÓXIMOS PASOS

Una vez configuradas las credenciales:

1. **Ejecuta el agente**:
   ```bash
   acm
   ```

2. **Analiza un artista real**:
   ```bash
   acm --artist "Los Chavalos de la Perla"
   ```

3. **Genera reportes con datos reales**:
   ```bash
   acm --artist "Los Chavalos de la Perla" --real-data --full-report
   ```

---

## ✅ CHECKLIST DE CONFIGURACIÓN

- [ ] Cuenta de Spotify Developer creada
- [ ] App de Spotify creada y credenciales copiadas
- [ ] Proyecto de Google Cloud creado
- [ ] YouTube Data API v3 habilitada
- [ ] API Key de YouTube obtenida
- [ ] Cuenta de Last.fm API creada
- [ ] API Key de Last.fm obtenida
- [ ] Configurador ejecutado (`--setup`)
- [ ] Credenciales probadas (`--test`)
- [ ] Todas las APIs con ✅ verde

---

**¡Listo! Ahora tu AGENTECATALOGOSMUSICALES tiene acceso a datos 100% reales de las principales plataformas musicales del mundo.**

---

*Creado: 2024*  
*Versión: 1.0 - Profesional*  
*Estado: Producción Ready ✅*
