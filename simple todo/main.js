
    const input = document.getElementById('todo-input');
    const addButton = document.getElementById('add-button');
    const todoList = document.getElementById('todo-list');

    let state = load();

    function save() {
      localStorage.setItem('state', JSON.stringify(state));
    }

    function load() {
      try {
        const saved = JSON.parse(localStorage.getItem('state'));
        if (
          saved &&
          typeof saved.keyCount === 'number' &&
          typeof saved.currentValue === 'string' &&
          Array.isArray(saved.todos)
        ) {
          return saved;
        }
      } catch (e) {}

      return {
        keyCount: 0,
        currentValue: '',
        todos: []
      };
    }

    function render() {
      todoList.innerHTML = '';
      state.todos.forEach(todo => {
        const div = document.createElement('div');
        div.className = 'todo-item';

        if (todo.isDone) div.style.textDecoration = 'line-through';

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = todo.isDone;
        checkbox.addEventListener('change', () => {
          todo.isDone = checkbox.checked;
          save();
          render();
        });

        const span = document.createElement('span');
        span.textContent = todo.text;

        const button = document.createElement('button');
        button.className = 'delete-button';
        button.textContent = '제거';
        button.addEventListener('click', () => {
          state.todos = state.todos.filter(t => t.key !== todo.key);
          save();
          render();
        });

        div.appendChild(checkbox);
        div.appendChild(span);
        div.appendChild(button);

        todoList.appendChild(div);
      });
    }

    input.addEventListener('input', (e) => {
      state.currentValue = e.target.value;
    });

    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') addTodo();
    });

    addButton.addEventListener('click', addTodo);

    function addTodo() {
      const text = state.currentValue.trim();
      if (text !== '') {
        state.todos.push({
          key: state.keyCount.toString(),
          isDone: false,
          text
        });
        state.keyCount++;
        state.currentValue = '';
        input.value = '';
        save();
        render();
      }
    }

    // 초기 렌더링
    input.value = state.currentValue;
    render();