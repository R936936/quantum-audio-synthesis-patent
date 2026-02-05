#!/usr/bin/env python3
"""
Fix para osciladores pulsados -> osciladores continuos sostenidos
Diagnóstico y corrección automática del código
"""

import re
import sys
from pathlib import Path

def diagnose_oscillator_issue(cpp_file):
    """Diagnosticar el problema de oscilación pulsada"""
    
    print("🔍 DIAGNOSTICANDO PROBLEMA DE OSCILACIÓN...")
    print("="*70)
    
    with open(cpp_file, 'r') as f:
        content = f.read()
    
    issues = []
    
    # 1. Buscar si oscAmount está siendo modulado por triggers
    if re.search(r'oscAmount.*trigger', content, re.IGNORECASE):
        issues.append("⚠️  oscAmount parece estar modulado por triggers")
    
    # 2. Buscar si los osciladores se resetean constantemente
    if content.count('osc.reset()') > 3:
        issues.append("⚠️  Los osciladores se resetean múltiples veces")
    
    # 3. Buscar envelopes que afecten amplitud
    env_matches = re.findall(r'(env[LRC]\d?\s*\*.*osc|osc.*env[LRC]\d?)', content)
    if env_matches:
        issues.append(f"⚠️  Encontrados {len(env_matches)} multiplicaciones de oscilador por envelope")
    
    # 4. Buscar amplitud pulsada
    if 'ampPulse' in content and 'process' in content:
        issues.append("⚠️  Se está usando ampPulse que puede causar pulsaciones")
    
    # 5. Verificar que oscAmount tiene valor por defecto
    osc_amount_match = re.search(r'configParam.*OSC_AMOUNT.*,\s*[\d.]+\s*,\s*[\d.]+\s*,\s*([\d.]+)', content)
    if osc_amount_match:
        default_val = float(osc_amount_match.group(1))
        if default_val < 0.5:
            issues.append(f"⚠️  OSC_AMOUNT default muy bajo: {default_val}")
        else:
            print(f"✅ OSC_AMOUNT default: {default_val}")
    
    return issues


def fix_oscillator_continuous(cpp_file, backup=True):
    """
    Corregir osciladores para que sean continuos sostenidos
    """
    
    print("\n🔧 APLICANDO CORRECCIONES...")
    print("="*70)
    
    if backup:
        backup_file = str(cpp_file) + '.backup_before_continuous_fix'
        Path(cpp_file).rename(backup_file)
        print(f"✅ Backup creado: {backup_file}")
    
    with open(backup_file if backup else cpp_file, 'r') as f:
        lines = f.readlines()
    
    corrections = 0
    new_lines = []
    
    for i, line in enumerate(lines):
        new_line = line
        
        # Corrección 1: Asegurar que oscAmount no se multiplica por envelopes para oscilación base
        # Buscamos líneas como: float spiralL = oscL.process(args.sampleTime) * oscAmount * envL1;
        if 'spiralL = oscL.process' in line and 'oscAmount' in line and 'env' in line:
            # Remover multiplicación por envelope
            new_line = re.sub(r'\s*\*\s*env[LRC]\d?', '', line)
            if new_line != line:
                print(f"🔧 Línea {i+1}: Removida modulación por envelope en oscilador L")
                corrections += 1
        
        elif 'spiralR = oscR.process' in line and 'oscAmount' in line and 'env' in line:
            new_line = re.sub(r'\s*\*\s*env[LRC]\d?', '', line)
            if new_line != line:
                print(f"🔧 Línea {i+1}: Removida modulación por envelope en oscilador R")
                corrections += 1
        
        elif 'spiralCenter = oscCenter.process' in line and 'oscAmount' in line and 'env' in line:
            new_line = re.sub(r'\s*\*\s*env[LRC]\d?', '', line)
            if new_line != line:
                print(f"🔧 Línea {i+1}: Removida modulación por envelope en oscilador Center")
                corrections += 1
        
        # Corrección 2: Comentar resets de osciladores que no sean necesarios
        # Mantener solo resets en el constructor
        if 'osc' in line.lower() and '.reset()' in line and 'constructor' not in lines[max(0, i-20):i]:
            # Si no está en un bloque de inicialización, comentar
            if not any(keyword in ''.join(lines[max(0, i-10):i]) for keyword in ['QuantumResonatorV3()', 'initialize', 'onReset']):
                if not line.strip().startswith('//'):
                    new_line = '//' + line
                    print(f"🔧 Línea {i+1}: Comentado reset innecesario de oscilador")
                    corrections += 1
        
        # Corrección 3: Verificar que amplitude pulses solo afecten gain adicional, no base
        if 'ampPulse' in line and '.get()' in line and 'spiral' in line:
            # Cambiar de multiplicación a suma
            if '*' in line and 'ampPulse' in line:
                new_line = re.sub(r'\*\s*ampPulse([LRC]|Center)?\.get\(\)', 
                                '+ ampPulse\\1.get() * 0.3', line)
                if new_line != line:
                    print(f"🔧 Línea {i+1}: Cambiado ampPulse de multiplicativo a aditivo")
                    corrections += 1
        
        new_lines.append(new_line)
    
    # Escribir archivo corregido
    with open(cpp_file, 'w') as f:
        f.writelines(new_lines)
    
    print(f"\n✅ Total de correcciones aplicadas: {corrections}")
    print(f"📁 Archivo actualizado: {cpp_file}")
    
    return corrections


def main():
    cpp_file = Path.home() / 'AurumLab' / 'src' / 'QuantumResonatorV3.cpp'
    
    if not cpp_file.exists():
        print(f"❌ Error: No se encuentra {cpp_file}")
        sys.exit(1)
    
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  FIX: Osciladores Pulsados → Osciladores Continuos Sostenidos   ║")
    print("╚══════════════════════════════════════════════════════════════════╝\n")
    
    # Diagnóstico
    issues = diagnose_oscillator_issue(cpp_file)
    
    if issues:
        print("\n❌ PROBLEMAS ENCONTRADOS:")
        for issue in issues:
            print(f"  {issue}")
    else:
        print("✅ No se encontraron problemas obvios en análisis estático")
    
    print("\n" + "="*70)
    response = input("\n¿Proceder con correcciones automáticas? (s/n): ").strip().lower()
    
    if response == 's':
        corrections = fix_oscillator_continuous(cpp_file, backup=True)
        
        print("\n" + "="*70)
        print("✅ CORRECCIONES COMPLETADAS")
        print("="*70)
        print("\n📋 PRÓXIMOS PASOS:")
        print("  1. Compilar módulo: cd ~/AurumLab && make -j4")
        print("  2. Probar en VCV Rack")
        print("  3. Si hay problemas, restaurar backup:")
        print(f"     cp {cpp_file}.backup_before_continuous_fix {cpp_file}")
    else:
        print("\n❌ Correcciones canceladas")


if __name__ == '__main__':
    main()
