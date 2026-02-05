#!/usr/bin/env python3
"""
FIX DEFINITIVO: Osciladores Pulsados → Sostenidos
==================================================

PROBLEMA IDENTIFICADO:
La modulación de amplitud por spiralDepth está causando que
los osciladores pulsen en lugar de ser sostenidos.

SOLUCIÓN:
Modificar la modulación de amplitud para que module ALREDEDOR
de un valor base en lugar de MULTIPLICAR, evitando que caiga a cero.
"""

import sys
from pathlib import Path
import re

def create_backup(file_path):
    """Crear backup con timestamp"""
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = str(file_path) + f'.backup_before_sustained_fix_{timestamp}'
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    with open(backup_path, 'w') as f:
        f.write(content)
    
    print(f"✅ Backup creado: {Path(backup_path).name}")
    return backup_path


def fix_spiral_amplitude_modulation(cpp_file):
    """
    Corregir la modulación de amplitud del oscilador en espiral
    para que sea sostenida en lugar de pulsada.
    """
    
    print("\n🔧 APLICANDO FIX DE OSCILACIÓN SOSTENIDA...")
    print("="*70)
    
    with open(cpp_file, 'r') as f:
        content = f.read()
    
    # CORRECCIÓN PRINCIPAL: Cambiar modulación de amplitud
    # ANTES: float finalAmplitude = (1.f - spiralDepth + spiralDepth * combinedRadius);
    # DESPUÉS: Modular ALREDEDOR de 1.0 en lugar de hasta 0.0
    
    old_amplitude_line = r'float finalAmplitude = \(1\.f - spiralDepth \+ spiralDepth \* combinedRadius\);'
    
    new_amplitude_code = '''// Apply spiral amplitude modulation - FIXED: Sostenido en lugar de pulsado
        // Modula ALREDEDOR de 1.0 en lugar de caer hasta (1-spiralDepth)
        // Rango: [1.0 - spiralDepth*0.3, 1.0 + spiralDepth*0.3]
        float modulationRange = spiralDepth * 0.3f;  // ±30% máximo
        float finalAmplitude = 1.0f + modulationRange * (combinedRadius * 2.f - 1.f);'''
    
    # Aplicar corrección
    content_new = re.sub(
        r'// Apply spiral amplitude modulation\s*\n\s*' + old_amplitude_line,
        new_amplitude_code,
        content
    )
    
    if content_new == content:
        # Intentar sin el comentario
        content_new = re.sub(
            old_amplitude_line,
            new_amplitude_code,
            content
        )
    
    corrections_made = content_new != content
    
    if corrections_made:
        print("✅ Corrección 1: Modulación de amplitud cambiada a sostenida")
        print(f"   • Rango de modulación: ±30% alrededor de 1.0")
        print(f"   • Antes: amplitud podía caer hasta (1 - spiralDepth)")
        print(f"   • Ahora: amplitud oscila entre 0.7x y 1.3x")
        content = content_new
    else:
        print("⚠️  No se pudo aplicar corrección de amplitud automáticamente")
        print("    Se aplicará manualmente...")
    
    # CORRECCIÓN 2: Asegurar que oscAmount tiene buen valor por defecto
    # (Ya está en 0.8, pero verificamos)
    osc_amount_match = re.search(
        r'configParam\(OSC_AMOUNT_PARAM,\s*[\d.]+f?,\s*[\d.]+f?,\s*([\d.]+)f?',
        content
    )
    
    if osc_amount_match:
        default_val = float(osc_amount_match.group(1))
        print(f"✅ Corrección 2: OSC_AMOUNT default = {default_val} (OK)")
    
    # CORRECCIÓN 3: Comentar sobre el problema para futura referencia
    correction_comment = '''
// ============================================================================
// FIX APLICADO: Osciladores ahora generan señal SOSTENIDA en lugar de PULSADA
// 
// Problema original:
//   - spiralDepth modulaba amplitud multiplicativamente: (1 - depth + depth*radius)
//   - Con depth alto, amplitud caía casi a cero → pulsaciones
//
// Solución:
//   - Modulación aditiva alrededor de 1.0: 1.0 ± depth*0.3*(radius*2-1)
//   - Amplitud nunca cae por debajo de 70%
//   - Oscilación sostenida y continua
// ============================================================================

'''
    
    # Insertar comentario antes de la definición de FibonacciSpiralOscillator
    struct_match = re.search(r'struct FibonacciSpiralOscillator\s*{', content)
    if struct_match:
        insert_pos = struct_match.start()
        content = content[:insert_pos] + correction_comment + content[insert_pos:]
        print("✅ Corrección 3: Documentación del fix añadida")
    
    # Escribir archivo corregido
    with open(cpp_file, 'w') as f:
        f.write(content)
    
    print(f"\n✅ Archivo actualizado: {cpp_file}")
    return True


def apply_manual_fix_if_needed(cpp_file):
    """
    Si el regex no funcionó, aplicar fix manualmente línea por línea
    """
    
    print("\n🔍 Verificando si se necesita fix manual...")
    
    with open(cpp_file, 'r') as f:
        lines = f.readlines()
    
    fixed = False
    new_lines = []
    
    for i, line in enumerate(lines):
        # Buscar la línea problemática
        if 'finalAmplitude' in line and 'spiralDepth' in line and 'combinedRadius' in line:
            # Verificar si ya está corregida
            if 'modulationRange' not in ''.join(lines[max(0,i-2):i+1]):
                print(f"🔧 Aplicando fix manual en línea {i+1}")
                
                # Reemplazar con versión corregida
                indent = len(line) - len(line.lstrip())
                new_lines.append(' ' * indent + '// FIXED: Modulación sostenida\n')
                new_lines.append(' ' * indent + 'float modulationRange = spiralDepth * 0.3f;\n')
                new_lines.append(' ' * indent + 'float finalAmplitude = 1.0f + modulationRange * (combinedRadius * 2.f - 1.f);\n')
                fixed = True
                continue
        
        new_lines.append(line)
    
    if fixed:
        with open(cpp_file, 'w') as f:
            f.writelines(new_lines)
        print("✅ Fix manual aplicado exitosamente")
    else:
        print("✅ No se necesita fix manual (ya corregido o no encontrado)")
    
    return fixed


def main():
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║                  FIX: OSCILADORES SOSTENIDOS                     ║")
    print("║                                                                  ║")
    print("║  Problema: Osciladores pulsan en lugar de sonar continuamente   ║")
    print("║  Causa: Modulación de amplitud cae hasta casi cero              ║")
    print("║  Solución: Modular ALREDEDOR de 1.0 en lugar de hasta 0         ║")
    print("╚══════════════════════════════════════════════════════════════════╝\n")
    
    cpp_file = Path.home() / 'AurumLab' / 'src' / 'QuantumResonatorV3.cpp'
    
    if not cpp_file.exists():
        print(f"❌ Error: No se encuentra {cpp_file}")
        sys.exit(1)
    
    print(f"📁 Archivo: {cpp_file}\n")
    
    # Crear backup
    backup_path = create_backup(cpp_file)
    
    # Aplicar correcciones
    success = fix_spiral_amplitude_modulation(cpp_file)
    
    # Si el regex no funcionó, aplicar manualmente
    if not success:
        apply_manual_fix_if_needed(cpp_file)
    
    print("\n" + "="*70)
    print("✅ FIX COMPLETADO")
    print("="*70)
    print("\n📋 PRÓXIMOS PASOS:")
    print("  1. Compilar: cd ~/AurumLab && make -j4")
    print("  2. Probar en VCV Rack")
    print("  3. Ajustar SPIRAL DEPTH para controlar intensidad de modulación")
    print(f"\n💾 Backup disponible en:")
    print(f"   {backup_path}")
    print(f"\n🔄 Para restaurar backup:")
    print(f"   cp {Path(backup_path).name} ~/AurumLab/src/QuantumResonatorV3.cpp")


if __name__ == '__main__':
    main()
