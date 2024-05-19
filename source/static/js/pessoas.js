function adicionar_pessoa() {
    const mainTableBody = document.getElementById('main-table-body');

    let newRegister = document.createElement('tr');
    newRegister.innerHTML = `
        <th scope="row">
            <input type="number" class="form-control" style="background-color: #D1D1D1  ;" disabled>
        </th>
        <td>
            <input type="text" class="form-control">
        </td>
        <td>
            <input type="text" class="form-control" style="background-color: #D1D1D1;" disabled>
        </td>
        <td>
            <input type="date" class="form-control">
        </td>
        <td style="text-align: center;">
            <button class="btn btn-success">
                <span class="material-icons">done</span>
            </button>
        </td>
        <td style="text-align: center;">
            <button class="btn btn-danger">
                <span class="material-icons">delete_forever</span>
            </button>
        </td>
    `;

    mainTableBody.append(newRegister);
}
