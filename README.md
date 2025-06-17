# PSI-Projekt: System rekomendacji filmów i seriali
Projekt na przedmiot PSI, rozwiązujący problem rekomendacji filmów i seriali na podstawie danych o produkcie.

## Zależności
Plik "requirements.txt" zawiera 4 biblioteki:
- numpy i pandas do przetwarzania danych
- faiss do wykrywania podobieństw między wektorami
- requests do komunikacji
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
2. włączyć program Ollama
3. Umieścić dane do nauki w pliku 'netflix_titles.csv'
4. Włączyć program Generate_index.py (nauka zajęła 4h)
5. Przejść do notebooka 'recomend.ipynb' i sprawdzić proste przykłady
