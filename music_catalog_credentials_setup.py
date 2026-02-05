#!/usr/bin/env python3
"""
CONFIGURADOR DE CREDENCIALES - AGENTECATALOGOSMUSICALES
Sistema profesional para configurar APIs de música reales
"""

import os
import json
import getpass
from pathlib import Path
from typing import Dict, Optional

class CredentialsManager:
    """Gestor de credenciales para APIs de música"""
    
    def __init__(self):
        self.home_dir = Path.home()
        self.config_dir = self.home_dir / ".agente_catalogos_musicales"
        self.config_file = self.config_dir / "credentials.json"
        self.env_file = self.config_dir / ".env"
        
    def setup(self):
        """Configuración inicial interactiva"""
        print("\n" + "="*80)
        print("  🎵 CONFIGURADOR DE CREDENCIALES - AGENTECATALOGOSMUSICALES")
        print("="*80)
        print("\nEste asistente te ayudará a configurar las credenciales para:")
        print("  • Spotify API (datos de streaming, popularidad, audio features)")
        print("  • YouTube Data API (visualizaciones, engagement)")
        print("  • Last.fm API (scrobbles, tendencias)")
        print("  • MusicBrainz (metadata de artistas y álbumes)")
        print("\n")
        
        # Crear directorio de configuración
        self.config_dir.mkdir(exist_ok=True)
        
        credentials = {}
        
        # Spotify
        print("━"*80)
        print("🎧 SPOTIFY API")
        print("━"*80)
        print("Para obtener credenciales:")
        print("  1. Ve a: https://developer.spotify.com/dashboard")
        print("  2. Inicia sesión con tu cuenta de Spotify")
        print("  3. Crea una nueva aplicación")
        print("  4. Copia el Client ID y Client Secret")
        print()
        
        spotify_enabled = input("¿Deseas configurar Spotify API? (s/n): ").lower() == 's'
        if spotify_enabled:
            spotify_client_id = input("  Spotify Client ID: ").strip()
            spotify_client_secret = getpass.getpass("  Spotify Client Secret: ").strip()
            
            credentials['spotify'] = {
                'enabled': True,
                'client_id': spotify_client_id,
                'client_secret': spotify_client_secret
            }
            print("  ✅ Spotify configurado correctamente")
        else:
            credentials['spotify'] = {'enabled': False}
            print("  ⏭️  Spotify omitido (se usarán datos demo)")
        
        # YouTube
        print("\n" + "━"*80)
        print("📺 YOUTUBE DATA API")
        print("━"*80)
        print("Para obtener credenciales:")
        print("  1. Ve a: https://console.cloud.google.com/")
        print("  2. Crea un nuevo proyecto o selecciona uno existente")
        print("  3. Habilita 'YouTube Data API v3'")
        print("  4. Ve a Credenciales > Crear Credenciales > Clave de API")
        print()
        
        youtube_enabled = input("¿Deseas configurar YouTube API? (s/n): ").lower() == 's'
        if youtube_enabled:
            youtube_api_key = getpass.getpass("  YouTube API Key: ").strip()
            
            credentials['youtube'] = {
                'enabled': True,
                'api_key': youtube_api_key
            }
            print("  ✅ YouTube configurado correctamente")
        else:
            credentials['youtube'] = {'enabled': False}
            print("  ⏭️  YouTube omitido (se usarán datos demo)")
        
        # Last.fm
        print("\n" + "━"*80)
        print("📻 LAST.FM API")
        print("━"*80)
        print("Para obtener credenciales:")
        print("  1. Ve a: https://www.last.fm/api/account/create")
        print("  2. Crea una aplicación")
        print("  3. Copia la API Key")
        print()
        
        lastfm_enabled = input("¿Deseas configurar Last.fm API? (s/n): ").lower() == 's'
        if lastfm_enabled:
            lastfm_api_key = input("  Last.fm API Key: ").strip()
            lastfm_shared_secret = getpass.getpass("  Last.fm Shared Secret (opcional): ").strip()
            
            credentials['lastfm'] = {
                'enabled': True,
                'api_key': lastfm_api_key,
                'shared_secret': lastfm_shared_secret if lastfm_shared_secret else None
            }
            print("  ✅ Last.fm configurado correctamente")
        else:
            credentials['lastfm'] = {'enabled': False}
            print("  ⏭️  Last.fm omitido (se usarán datos demo)")
        
        # MusicBrainz (no requiere credenciales pero es bueno configurar el user-agent)
        print("\n" + "━"*80)
        print("🎼 MUSICBRAINZ API")
        print("━"*80)
        print("MusicBrainz no requiere API key, pero necesita un User-Agent.")
        print()
        
        app_name = input("  Nombre de tu aplicación (ej: AgenteCatalogos/1.0): ").strip()
        contact_email = input("  Email de contacto: ").strip()
        
        credentials['musicbrainz'] = {
            'enabled': True,
            'app_name': app_name or "AgenteCatalogosMusicales/1.0",
            'contact': contact_email or "user@example.com"
        }
        print("  ✅ MusicBrainz configurado correctamente")
        
        # Guardar credenciales
        self._save_credentials(credentials)
        self._create_env_file(credentials)
        
        print("\n" + "="*80)
        print("  ✅ CONFIGURACIÓN COMPLETADA EXITOSAMENTE")
        print("="*80)
        print(f"\nCredenciales guardadas en:")
        print(f"  📁 {self.config_file}")
        print(f"  📁 {self.env_file}")
        print("\n¡El agente ahora podrá acceder a datos reales de las APIs configuradas!")
        print("\nPara verificar tu configuración, ejecuta:")
        print("  python3 music_catalog_credentials_setup.py --test")
        print()
        
    def _save_credentials(self, credentials: Dict):
        """Guardar credenciales en archivo JSON"""
        with open(self.config_file, 'w') as f:
            json.dump(credentials, f, indent=2)
        
        # Proteger archivo con permisos restrictivos
        os.chmod(self.config_file, 0o600)
        
    def _create_env_file(self, credentials: Dict):
        """Crear archivo .env para variables de entorno"""
        env_lines = [
            "# AGENTECATALOGOSMUSICALES - Credenciales de APIs",
            "# Generado automáticamente - NO COMPARTIR",
            ""
        ]
        
        if credentials.get('spotify', {}).get('enabled'):
            env_lines.extend([
                "# Spotify API",
                f"SPOTIFY_CLIENT_ID={credentials['spotify']['client_id']}",
                f"SPOTIFY_CLIENT_SECRET={credentials['spotify']['client_secret']}",
                ""
            ])
        
        if credentials.get('youtube', {}).get('enabled'):
            env_lines.extend([
                "# YouTube Data API",
                f"YOUTUBE_API_KEY={credentials['youtube']['api_key']}",
                ""
            ])
        
        if credentials.get('lastfm', {}).get('enabled'):
            env_lines.extend([
                "# Last.fm API",
                f"LASTFM_API_KEY={credentials['lastfm']['api_key']}",
            ])
            if credentials['lastfm'].get('shared_secret'):
                env_lines.append(f"LASTFM_SHARED_SECRET={credentials['lastfm']['shared_secret']}")
            env_lines.append("")
        
        if credentials.get('musicbrainz', {}).get('enabled'):
            env_lines.extend([
                "# MusicBrainz API",
                f"MUSICBRAINZ_APP_NAME={credentials['musicbrainz']['app_name']}",
                f"MUSICBRAINZ_CONTACT={credentials['musicbrainz']['contact']}",
                ""
            ])
        
        with open(self.env_file, 'w') as f:
            f.write('\n'.join(env_lines))
        
        # Proteger archivo .env
        os.chmod(self.env_file, 0o600)
    
    def test_credentials(self):
        """Probar credenciales configuradas"""
        print("\n" + "="*80)
        print("  🧪 PROBANDO CREDENCIALES")
        print("="*80 + "\n")
        
        if not self.config_file.exists():
            print("❌ No hay credenciales configuradas.")
            print("   Ejecuta: python3 music_catalog_credentials_setup.py --setup")
            return
        
        with open(self.config_file, 'r') as f:
            credentials = json.load(f)
        
        # Test Spotify
        if credentials.get('spotify', {}).get('enabled'):
            print("🎧 Probando Spotify API...")
            try:
                import requests
                import base64
                
                client_id = credentials['spotify']['client_id']
                client_secret = credentials['spotify']['client_secret']
                
                auth_str = f"{client_id}:{client_secret}"
                auth_b64 = base64.b64encode(auth_str.encode()).decode()
                
                response = requests.post(
                    "https://accounts.spotify.com/api/token",
                    headers={"Authorization": f"Basic {auth_b64}"},
                    data={"grant_type": "client_credentials"},
                    timeout=10
                )
                
                if response.status_code == 200:
                    print("  ✅ Spotify: Conexión exitosa")
                else:
                    print(f"  ❌ Spotify: Error {response.status_code}")
            except Exception as e:
                print(f"  ❌ Spotify: Error - {str(e)}")
        else:
            print("  ⏭️  Spotify: No configurado")
        
        # Test YouTube
        if credentials.get('youtube', {}).get('enabled'):
            print("\n📺 Probando YouTube API...")
            try:
                import requests
                
                api_key = credentials['youtube']['api_key']
                response = requests.get(
                    "https://www.googleapis.com/youtube/v3/search",
                    params={
                        "part": "snippet",
                        "q": "test",
                        "maxResults": 1,
                        "key": api_key
                    },
                    timeout=10
                )
                
                if response.status_code == 200:
                    print("  ✅ YouTube: Conexión exitosa")
                else:
                    print(f"  ❌ YouTube: Error {response.status_code}")
            except Exception as e:
                print(f"  ❌ YouTube: Error - {str(e)}")
        else:
            print("  ⏭️  YouTube: No configurado")
        
        # Test Last.fm
        if credentials.get('lastfm', {}).get('enabled'):
            print("\n📻 Probando Last.fm API...")
            try:
                import requests
                
                api_key = credentials['lastfm']['api_key']
                response = requests.get(
                    "http://ws.audioscrobbler.com/2.0/",
                    params={
                        "method": "chart.gettopartists",
                        "api_key": api_key,
                        "format": "json",
                        "limit": 1
                    },
                    timeout=10
                )
                
                if response.status_code == 200:
                    print("  ✅ Last.fm: Conexión exitosa")
                else:
                    print(f"  ❌ Last.fm: Error {response.status_code}")
            except Exception as e:
                print(f"  ❌ Last.fm: Error - {str(e)}")
        else:
            print("  ⏭️  Last.fm: No configurado")
        
        # MusicBrainz siempre está disponible
        print("\n🎼 Probando MusicBrainz API...")
        try:
            import requests
            
            app_name = credentials.get('musicbrainz', {}).get('app_name', 'Test/1.0')
            contact = credentials.get('musicbrainz', {}).get('contact', 'test@example.com')
            
            response = requests.get(
                "https://musicbrainz.org/ws/2/artist/",
                params={"query": "artist:test", "limit": 1, "fmt": "json"},
                headers={"User-Agent": f"{app_name} ( {contact} )"},
                timeout=10
            )
            
            if response.status_code == 200:
                print("  ✅ MusicBrainz: Conexión exitosa")
            else:
                print(f"  ❌ MusicBrainz: Error {response.status_code}")
        except Exception as e:
            print(f"  ❌ MusicBrainz: Error - {str(e)}")
        
        print("\n" + "="*80)
        print("  PRUEBAS COMPLETADAS")
        print("="*80 + "\n")
    
    def show_status(self):
        """Mostrar estado de configuración"""
        print("\n" + "="*80)
        print("  📊 ESTADO DE CONFIGURACIÓN")
        print("="*80 + "\n")
        
        if not self.config_file.exists():
            print("❌ No hay credenciales configuradas.")
            print("\nPara configurar las credenciales, ejecuta:")
            print("  python3 music_catalog_credentials_setup.py --setup")
            return
        
        with open(self.config_file, 'r') as f:
            credentials = json.load(f)
        
        print("APIs configuradas:\n")
        
        apis = [
            ('Spotify', 'spotify', '🎧'),
            ('YouTube', 'youtube', '📺'),
            ('Last.fm', 'lastfm', '📻'),
            ('MusicBrainz', 'musicbrainz', '🎼')
        ]
        
        for name, key, icon in apis:
            if credentials.get(key, {}).get('enabled'):
                print(f"  {icon} {name:15} ✅ Configurado")
            else:
                print(f"  {icon} {name:15} ⏭️  No configurado (modo demo)")
        
        print("\n" + "="*80 + "\n")
        print(f"Archivo de configuración: {self.config_file}")
        print(f"Archivo de entorno:       {self.env_file}")
        print("\nPara probar las credenciales:")
        print("  python3 music_catalog_credentials_setup.py --test")
        print()


def main():
    """Función principal"""
    import sys
    
    manager = CredentialsManager()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--setup':
            manager.setup()
        elif sys.argv[1] == '--test':
            manager.test_credentials()
        elif sys.argv[1] == '--status':
            manager.show_status()
        else:
            print("Uso:")
            print("  python3 music_catalog_credentials_setup.py --setup    # Configurar credenciales")
            print("  python3 music_catalog_credentials_setup.py --test     # Probar credenciales")
            print("  python3 music_catalog_credentials_setup.py --status   # Ver estado")
    else:
        # Modo interactivo por defecto
        print("\n🎵 GESTOR DE CREDENCIALES - AGENTECATALOGOSMUSICALES\n")
        print("Selecciona una opción:")
        print("  1. Configurar credenciales")
        print("  2. Probar credenciales")
        print("  3. Ver estado")
        print("  4. Salir")
        print()
        
        choice = input("Opción: ").strip()
        
        if choice == '1':
            manager.setup()
        elif choice == '2':
            manager.test_credentials()
        elif choice == '3':
            manager.show_status()
        elif choice == '4':
            print("👋 ¡Hasta luego!")
        else:
            print("❌ Opción no válida")


if __name__ == "__main__":
    main()
