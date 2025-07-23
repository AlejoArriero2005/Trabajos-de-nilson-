<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Calculadora</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
        }
        form {
            background-color: #f4f4f4;
            padding: 20px;
            border-radius: 10px;
            width: 300px;
        }
        input, select {
            padding: 8px;
            margin-top: 10px;
            width: 100%;
        }
        .resultado {
            margin-top: 15px;
            font-weight: bold;
        }
    </style>
</head>
<body>

<h2>Calculadora Fesna</h2>

<form method="post">
    <label for="num1">Número 1:</label>
    <input type="number" name="num1" required>

    <label for="num2">Número 2:</label>
    <input type="number" name="num2" required>

    <label for="operacion">Operación:</label>
    <select name="operacion" required>
        <option value="sumar">Sumar (+)</option>
        <option value="restar">Restar (-)</option>
        <option value="multiplicar">Multiplicar (*)</option>
        <option value="dividir">Dividir (/)</option>
    </select>

    <input type="submit" name="calcular" value="Calcular">

    <?php
    if (isset($_POST['calcular'])) {
        $num1 = $_POST['num1'];
        $num2 = $_POST['num2'];
        $operacion = $_POST['operacion'];
        $resultado = '';

        switch ($operacion) {
            case 'sumar':
                $resultado = $num1 + $num2;
                break;
            case 'restar':
                $resultado = $num1 - $num2;
                break;
            case 'multiplicar':
                $resultado = $num1 * $num2;
                break;
            case 'dividir':
                if ($num2 != 0) {
                    $resultado = $num1 / $num2;
                } else {
                    $resultado = 'Error: División por cero';
                }
                break;
            default:
                $resultado = 'Operación inválida';
        }

        echo "<div class='resultado'>Resultado: $resultado</div>";
    }
    ?>
</form>

</body>
</html>