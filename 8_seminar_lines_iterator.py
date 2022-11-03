class FileIterator:
    def __init__(self, file_path: str):
      with open(file_path, 'r', encoding='utf8') as f:
        self.file = list(f)
      self.max_iter = len(self.file)
      self.current_iter = 0

    def __iter__(self):
      return self

    def __next__(self):
      if self.current_iter < self.max_iter:
        self.current_iter += 1
        return self.file[self.current_iter - 1]
      raise StopIteration


first_letters = list()

for line in FileIterator("Waxwork.1988.720p.English.srt"):
    stripped_line = line.strip()
    first_letters.append(stripped_line[0])

possibly_some_encrypted_message = ''.join(first_letters)

print(f"First letters of the file's lines make up the following text: \"{possibly_some_encrypted_message}\".")
