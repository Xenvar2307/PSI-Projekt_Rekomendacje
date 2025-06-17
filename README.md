# PSI-Projekt: System rekomendacji filmów i seriali
Projekt na przedmiot PSI, rozwiązujący problem rekomendacji filmów i seriali na podstawie danych o produkcie.

## Schemat działania
Program opiera się na Large Language Model LLama2 od Mety. Opisy produktów są zamieniane na pojedynczy String, następnie za pomocą modelu językowego, zamieniane na wektory (podobne w znaczeniu frazy będą znajdowały się bliżej siebie). Na takich wektorach może operować indexFlatL2, który ma za zadanie obliczyć odległości euklidesowe między nimi, co może być powolne, ale za to dokładne. 

## Zależności
Plik "requirements.txt" zawiera 4 biblioteki:
- numpy i pandas do przetwarzania danych
- faiss do wykrywania podobieństw między wektorami
- requests do komunikacji\
Dodatkowo embedding opisu produktów jest wykonywany za pomocą modelu llama2 z Ollama, jeżeli chcemy samemu nauczyć algorytm należy go zainstalować według instrukcji w pliku z wymaganiami

___

## Pliki
- my_util_func.py - zawiera funkcje pomocnicze, wydzielone dla przejrzystości kodu
- requirements.txt - patrz wyżej
- Generate_index.py - program tworzący plik Index z wektorami (embedding)
- recomend.ipynb - notebook z funkcją znajdującą n najlepszych dopasować wektorów (produktów) na podstawie tekstowej reprezentacji produktu
- netflix_titles.csv - ponad 8 tysięcy produktów z bazy kaggle: https://www.kaggle.com/datasets/shivamb/netflix-shows

___

## Instrukcje nauczania
1. Upewnij się że spełniasz wymagania
`pip install -r requirements.txt`
`Ollama pull llama2`
3. włączyć program Ollama
4. Umieścić dane do nauki w pliku 'netflix_titles.csv'
5. Włączyć program Generate_index.py (nauka zajęła 4h)
6. Przejść do notebooka 'recomend.ipynb' i sprawdzić proste przykłady
