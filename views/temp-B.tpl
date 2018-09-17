<!DOCTYPE <!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Hasar</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    % include("haus.tpl")
    <div class="row">
        <section><h2>FORSÍÐA</h2></section>
        <section><h2>Nýjustu fréttir!</h2></section>
        <section><img src="/static/franku.jpg" alt="filthy frank"></section>
        <section>
            <ul>
                <li><a href="/frett/0">Irma veldur Usla í Florida</a></li>
                <li><a href="/frett/1">Veiðin er dræm þetta haustið</a></li>
                <li><a href="/frett/2">Ólafía stendur sig vel</a></li>
                <li><a href="/frett/3">Ísland dottið úr leik</a></li>
            </ul>
        </section>
    </div>
    % include("footer.tpl")
    % end
</body>
</html>