#!/usr/bin/env python3
import urllib.request
import sys

# URLs directas de imágenes IBM Quantum conocidas
urls = [
    # IBM Quantum System One
    "https://www.ibm.com/blogs/research/wp-content/uploads/2019/01/7H1A0200-1.jpg",
    # IBM Quantum Lab
    "https://www.ibm.com/blogs/research/wp-content/uploads/2020/09/quantum-roadmap-header.jpg",
    # Alternative
    "https://raw.githubusercontent.com/Qiskit/qiskit/main/docs/images/ibm_quantum_logo.png"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
}

for i, url in enumerate(urls):
    try:
        print(f"Intentando URL {i+1}: {url}")
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req, timeout=10)
        
        content_type = response.headers.get('Content-Type', '')
        print(f"  Content-Type: {content_type}")
        
        if 'image' in content_type:
            data = response.read()
            ext = 'jpg' if 'jpeg' in content_type else 'png'
            filename = f'/Users/wu/ibm_quantum_hardware.{ext}'
            
            with open(filename, 'wb') as f:
                f.write(data)
            
            print(f"✅ Imagen descargada: {filename} ({len(data)} bytes)")
            sys.exit(0)
        else:
            print(f"  ❌ No es imagen: {content_type}")
            
    except Exception as e:
        print(f"  ❌ Error: {e}")

print("\n❌ No se pudo descargar ninguna imagen")
sys.exit(1)
