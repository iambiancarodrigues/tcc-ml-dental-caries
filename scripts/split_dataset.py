import os
import random

# Diretório com as imagens do tipo (a)
IMAGE_DIR = "data/raw/images"

# Caminhos dos arquivos de saída com os splits
OUTPUT_DIR = "data/splits/"
TRAIN_SPLIT_FILE = os.path.join(OUTPUT_DIR, "train_split.txt")
VAL_SPLIT_FILE = os.path.join(OUTPUT_DIR, "val_split.txt")
TEST_SPLIT_FILE = os.path.join(OUTPUT_DIR, "test_split.txt")

# Proporções
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

def main():
    # Lista todas as imagens .png da pasta
    images = [f for f in os.listdir(IMAGE_DIR) if f.endswith(".png")]
    images.sort()  # para manter determinístico antes do shuffle
    random.seed(42)
    random.shuffle(images)

    total = len(images)
    train_end = int(total * train_ratio)
    val_end = train_end + int(total * val_ratio)

    train_images = images[:train_end]
    val_images = images[train_end:val_end]
    test_images = images[val_end:]

    # Salva os nomes dos arquivos (sem caminho)
    with open(TRAIN_SPLIT_FILE, "w") as f:
        f.write("\n".join(train_images))
    with open(VAL_SPLIT_FILE, "w") as f:
        f.write("\n".join(val_images))
    with open(TEST_SPLIT_FILE, "w") as f:
        f.write("\n".join(test_images))

    print(f"✅ Split concluído com sucesso:")
    print(f"  Treinamento: {len(train_images)} imagens")
    print(f"  Validação:  {len(val_images)} imagens")
    print(f"  Teste:      {len(test_images)} imagens")

if __name__ == "__main__":
    main()
