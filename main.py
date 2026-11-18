import json
from pathlib import Path
from wer import compute_wer_metrics

def main():
    print("Hello from homework4!")

    with open("reference.txt", "r", encoding="utf-8") as f:
        reference_text = f.read()

    with open("hypothesis.txt", "r", encoding="utf-8") as f:
        hypothesis_text = f.read()

    metrics = compute_wer_metrics(reference_text, hypothesis_text)
    
    output_filename = "wer_results.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=4, ensure_ascii=False)

    print(f"Метрики збережено у файл {output_filename}")
    print(json.dumps(metrics, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()