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
        <section><h2>{{ frett[0] }}</h2></section>
        <section><h2>Fréttir</h2></section>
        <section><img src="/static/{{ frett[2] }}" alt="mynd_0"></section>
        <section>
            <p>{{ frett[1] }}</p>
            <p>Höfundur: {{ frett[3] }}</p>
            <h4><a href="/b">Aftur á forsíðu</a></h4>
        </section>
    </div>
    % include("footer.tpl")
    % end
</body>
</html>