class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Tarefa "{task}" adicionada com sucesso!')

    def view_tasks(self):
        if not self.tasks:
            print('Nenhuma tarefa na lista.')
        else:
            print(' ' * 20)
            print('Tarefas:')
            print('-' * 20)
            for i, task in enumerate(self.tasks, 1):
                print(f'{i}. {task}')

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f'Tarefa "{removed_task}" removida com sucesso!')
        else:
            print('Índice inválido.')

def main():
    todo_list = ToDoList()

    while True:
        print('\n1. Adicionar Tarefa\n2. Ver Tarefas\n3. Remover Tarefa\n4. Sair')
        choice = input('Escolha uma opção: ')

        if choice == '1':
            task = input('Digite a nova tarefa: ')
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input('Digite o número da tarefa a ser removida: '))
            todo_list.remove_task(index)
        elif choice == '4':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()
