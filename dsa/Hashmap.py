class HashMap:
    def __init__(self, size=10):
        """Inicializa o HashMap com um array fixo e listas para lidar com colisões."""
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """
        Função de hash simples: calcula o índice baseado na soma dos caracteres da chave.
        Retorna o índice no intervalo [0, size-1].
        """
        return sum(ord(char) for char in str(key)) % self.size

    def insert(self, key, value):
        """
        Insere um par (chave, valor) no HashMap.
        Se a chave já existir, atualiza o valor.
        """
        index = self._hash(key)  # Calcula o índice usando a função de hash
        bucket = self.table[index]

        # Verifica se a chave já existe no bucket
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Atualiza o valor
                return

        # Se a chave não existir, adiciona ao bucket
        bucket.append((key, value))

    def get(self, key):
        """
        Retorna o valor associado à chave.
        Lança KeyError se a chave não for encontrada.
        """
        index = self._hash(key)  # Calcula o índice usando a função de hash
        bucket = self.table[index]

        # Procura a chave no bucket
        for k, v in bucket:
            if k == key:
                return v

        # Se não encontrar, lança um erro
        raise KeyError(f"Key '{key}' not found in HashMap.")

    def delete(self, key):
        """
        Remove o par (chave, valor) do HashMap.
        Lança KeyError se a chave não for encontrada.
        """
        index = self._hash(key)  # Calcula o índice usando a função de hash
        bucket = self.table[index]

        # Procura a chave no bucket e remove
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

        # Se não encontrar, lança um erro
        raise KeyError(f"Key '{key}' not found in HashMap.")

    def display(self):
        """Exibe o estado atual do HashMap."""
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")
            

# Cria o HashMap
hashmap = HashMap(size=5)

# Insere pares chave-valor
hashmap.insert("name", "Alice")
hashmap.insert("age", 30)
hashmap.insert("city", "New York")
hashmap.insert("email", "alice@example.com")

# Exibe o estado do HashMap
print("HashMap atual:")
hashmap.display()

# Atualiza o valor para a chave "name"
hashmap.insert("name", "Bob")

# Busca por chaves
print("\nBusca de elementos:")
print("name:", hashmap.get("name"))
print("age:", hashmap.get("age"))

# Remove um elemento
print("\nRemovendo 'city'...")
hashmap.delete("city")
hashmap.display()

# Tentativa de buscar chave inexistente
try:
    print(hashmap.get("city"))
except KeyError as e:
    print("\nErro:", e)
