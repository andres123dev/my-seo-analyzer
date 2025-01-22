# my-seo-analyzer 

<div align="center">
  <table border="0" cellpadding="0" cellspacing="0">
    <tbody>
      <tr>
        <th>Proyect</th>
        <td>my-seo-analyzer</td>
      </tr>
      <tr>
        <th>Description</th>
		    <td>Script to request a HTML webpage, analyze the SEO of the response and generate a report in PDF format.</td>
      </tr>
      <tr>
        <th>Author</th>
        <td>Andrés Fernández Burón</td>
      </tr>
      <tr>
        <th>Copyright</th>
        <td>2023-2025 &copy; All rights reserved</td>
      </tr>
    </tbody>
  </table>
</div>

<div>
<hr>
<pre>
          _____________________________________
         / ================================== /|
        / ========= MY SEO analyzer ======== /||
       / ================================== /|||
      /                                    /||||
     /  Request to an URL for a HTML,     /|||||
    /  analyze the SEO of the document   /||||||
   /  and generate a report in PDF      /|||||||
  /____________________________________////////
 |                                     |//////
 | Andres Fernandez Buron              |/////
 |                                     |////
 | Copyright (C) 2022                  |///
 | All rights reserved                 |//
 |_____________________________________|/
</pre>
<hr>
</div>

<div id="index" align="right">
	<b>Language:</b> <a href="#index-es">Español</a> | <a href="#index-en">English</a>
</div>

<hr>

<div id="index-es">

## Índice

- Descripción
- Requisitos
- Dependencias
- Instalación
- Ejemplos de uso
- Compatibilidad

</div>

<div id="readme-es">  

## Descripción
<b>My SEO analyzer</b> es un script escrito con <a href="https://www.python.org/doc/" target="_blank">Python 3</a>.

<b>My SEO analyzer</b> sirve para realizar una petición HTTP a una URL, analizar el SEO del documento HTML y generar un reporte en formato PDF.

<b>My SEO analyzer</b> analiza la respuesta HTTP y el documento HTML.

- Las cabeceras HTTP de la respuesta
- Las meta etiquetas
- Los títulos
- El DOM del documento HTML
- El texto
- Los links
  
## Requisitos
<b>My SEO analyzer</b> requiere tener instalado el lenguaje <a href="https://www.python.org/downloads/" target="_blank">Python 3</a> y <a href="" target="_blank">Pip</a>.
  
## Dependencias
<b>My SEO analyzer</b> depende de los siguientes módulos de Python 3:  

- <a href="https://requests.readthedocs.io/en/latest/" target="_blank">Requests</a>
- <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="_blank">BeautifulSoup4</a>
- <a href="https://lxml.de/index.html#documentation" target="_blank">lxml</a>
- <a href="" target="_blank">ReportLab</a>  

Instalar las dependencias manualmente con Pip:  
<code> pip install request, lxml, bs4, reportlab </code>  

Instalar las dependencias desde requirements.txt:  
<code> pip install -r requirements.txt </code>
  
## Instalación  

<b>My SEO analyzer</b> no necesita instalación</a>.    

Mostrar versión:  
<code> python my_seo_analyzer -v </code>  
<code> python my_seo_analyzer --version </code>  

Mostrar ayuda::  
<code> python my_seo_analyzer -h </code>  
<code> python my_seo_analyzer --help </code> 
  
## Ejemplos de uso  

<b>My SEO analyzer</b> se ejecuta cómo cualquier otro script de Python 3.  

Ejemplos de peticiones HTTP:  
<code> python my_seo_analyzer -url paginaweb.com </code>  
<code> python my_seo_analyzer -url <a>http://paginaweb.com/</a> </code>  

Ejemplos de peticiones HTTPS:  
<code> python my_seo_analyzer -url paginaweb.com -https </code>  
<code> python my_seo_analyzer -url <a>https://paginaweb.com/</a> </code>  
  
## Compatibilidad  

Este script es multiplataforma.

<div align="center">

| OS      | Soportado  |
|---------|------------|
| Unix    | &#10004; |
| Linux   | &#10004; |
| Windows | &#10004; |
| MAC     | Sin probar |

</div>

</div>

<hr>

<div id="index-en">

## Index

- Description
- Requirements
- Dependencies
- Installation
- Use
- Compatibility

</div>

<div id="readme-en">

## Description
Is an interactive consol app wrote with <a href="https://www.python.org/downloads/" target="_blank">Python 3</a>, to make a HTTP request to an URL, analyze SEO of the response HTML and generate a report in PDF format.  

- The HTTP headers of the response
- The meta tags
- The titles
- The DOM of the HTML document
- The text content
- The links 
  
## Requirements

<b>My SEO analyzer</b> require to have intalled <a href="https://www.python.org/downloads/" target="_blank">Python 3</a> language and <a href="">Pip</a>.
  
## Dependencies

<b>My SEO analyzer</b> depends on the following Python libraries:  

- <a href="https://requests.readthedocs.io/en/latest/" target="_blank">Requests</a>
- <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="_blank">BeautifulSoup4</a>
- <a href="https://lxml.de/index.html#documentation" target="_blank">lxml</a>
- <a href="" target="_blank">ReportLab</a>  

Install the dependencies manually with Pip:  
<code> pip install request, lxml, bs4, reportlab </code>  

Or install all dependencies from requirements.txt:  
<code> pip install -r requirements.txt </code>  
  
## Installation
<b>My SEO analyzer</b> doesn't need installation.  

Show version:  
<code> python my_seo_analyzer -v </code>  
<code> python my_seo_analyzer --version </code>

Show help:  
<code> python my_seo_analyzer -h </code>  
<code> python my_seo_analyzer --help </code>  

## Examples of use

<b>My SEO analyzer</b> runs like any other Python 3 script.   

HTTP request examples:  
<code> python my_seo_analyzer -url webpage.com </code>  
<code> python my_seo_analyzer -url <a>http://webpage.com/</a> </code>  

HTTPS request examples:  
<code> python my_seo_analyzer -url webpage.com -https </code>  
<code> python my_seo_analyzer -url <a>https://webpage.com/</a> </code>  
  
## Compatibility

<b>My SEO analyzer</b> is multiplatform script.

<div align="center">  

| OS      | Compatibility |
|---------|---------------|
| Unix    | &#10004; |
| Linux   | &#10004; |
| Windows | &#10004; |
| MAC     | Not tested |
  
</div>

</div>
