from ursina import *
import pandas as pd
import numpy as np
import hashlib

app = Ursina(title="SPHY AUDIT - Transição de Fase", size=(1920, 1080))
window.color = color.black

# --- CARGA E INFRAESTRUTURA ---
df = pd.read_parquet("sphy_slit_audit.parquet")
num_frames = df['frame'].max() + 1
particles_per_frame = len(df) // num_frames

cloud = Entity(
    model=Mesh(
        vertices=[(0,0,0)] * particles_per_frame,
        colors=[color.cyan] * particles_per_frame,
        mode='point',
        thickness=0.018
    ),
    unlit=True
)

# HUD de Soberania
status_txt = Text(text="AUDIT: STARTING", position=(-0.85, 0.45), scale=1.5)
hash_txt = Text(text="HASH: NULL", position=(-0.85, 0.40), scale=0.7, color=color.gray)
timer_txt = Text(text="TIMER: 0.0s", position=(-0.85, 0.35), scale=1, color=color.yellow)

# Controles na Tela
Text(text="CONTROLES:", position=(0.6, 0.45), color=color.gold, scale=0.8)
Text(text="[DIR] Rotacionar", position=(0.6, 0.41), scale=0.7)
Text(text="[ESQ] Mover (Pan)", position=(0.6, 0.38), scale=0.7)
Text(text="[R] Reset Câmera", position=(0.6, 0.35), scale=0.7)

current_frame = 0

def update():
    global current_frame
    
    # Extração e Validação
    frame_data = df[df['frame'] == current_frame]
    pos = frame_data[['x', 'y', 'z']].values
    
    # Verificação de Integridade Criptográfica
    current_bytes = pos.astype(np.float32).tobytes()
    calc_hash = hashlib.sha256(current_bytes).hexdigest()
    orig_hash = frame_data['hash'].iloc[0]
    
    # Lógica de Visualização por Frame
    is_collapsed = current_frame > (num_frames / 2)
    elapsed_time = current_frame / 30.0 # Simulação baseada em 30 FPS
    
    if calc_hash == orig_hash:
        status_txt.text = "AUDIT: VERIFIED [OK]"
        status_txt.color = color.green if not is_collapsed else color.gold
    else:
        status_txt.text = "AUDIT: TAMPERED [FAIL]"
        status_txt.color = color.red
        
    hash_txt.text = f"SHA256: {calc_hash}"
    timer_txt.text = f"TEMPO: {elapsed_time:.1f}s / 30.0s"
    
    # Atualiza a Mesh
    cloud.model.vertices = pos.tolist()
    cloud.model.colors = [color.cyan if not is_collapsed else color.gold for _ in range(particles_per_frame)]
    cloud.model.generate()
    
    current_frame = (current_frame + 1) % num_frames

# Configuração de Câmera (Adaptada ao Hardware)
camera.z = -70
ec = EditorCamera()
ec.pan_button = 'left mouse'
ec.rotation_button = 'right mouse'

def input(key):
    if key == 'r': camera.position, camera.rotation = (0,0,-70), (0,0,0)

app.run()
