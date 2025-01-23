# my-seo-analyzer 

<div align="center">
  <table border="0" cellpadding="0" cellspacing="0">
    <tbody>
      <tr> <th>Proyect</th> <td>My SEO analyzer</td>  </tr>
      <tr>
        <th>Description</th>
	      <td>Script to request a HTML webpage, analyze the SEO of the response and generate a report in PDF format.</td>
      </tr>
      <tr> <th>Author</th> <td>Andrés Fernández Burón</td> </tr>
      <tr> <th>Copyright</th> <td>2023-2025 &copy; All rights reserved</td> </tr>
    </tbody>
  </table>
</div>

<div align="right">
	<b>Language:</b> <a href="#index-es">Español</a> | <a href="#index-en">English</a>
</div>

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

<div id="index-es">

## Índice  

1. [Descripcion](#descripcion)  
2. [Requisitos](#requisitos)  
3. [Dependencias](#dependencias)  
4. [Descarga](#descarga)  
5. [Instalacion](#instalacion)  
6. [Ejemplos de uso](#ejemplos-de-uso)  
7. [Compatibilidad](#compatibilidad)  

</div>

<div id="readme-es">  

## Descripcion

<b>My SEO analyzer</b> permite realizar una petición a un documento HTML, analizar el SEO de la respuesta HTTP y generar un reporte en formato PDF.  

Analiza la respuesta HTTP y el documento HTML.  

- Las cabeceras HTTP de la respuesta  
- Las meta etiquetas  
- Los títulos  
- El DOM del documento HTML  
- El texto  
- Los links  
  
## Requisitos

<b>My SEO analyzer</b> está escrito con [Python](https://www.python.org/doc/), y requiere tener instalado el lenguaje [Python 3](https://www.python.org/downloads/) y [Pip]().

## Dependencias
<b>My SEO analyzer</b> depende de los siguientes módulos Python de terceros:  

- [Requests](https://requests.readthedocs.io/en/latest/)  
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  
- [lxml](https://lxml.de/index.html#documentation)  
- [ReportLab]()  

 Si no sabes instalar las dependencias, consulta este [manual](../apuntes-andres/python/pip.md#instalar-módulos-desde-requirementstxt).  


## Descarga

Puedes descargar <b>My SEO analyzer</b> mediante una aplicación cliente cómo ````GitBash````. 

También puedes descargarlo cómo fichero ZIP  [my-seo-analyzer-main.zip](https://github.com/andres123dev/my-seo-analyzer/archive/refs/heads/main.zip)

> Si tienes alguna duda, consulta este [manual](../apuntes-andres/github/descargar-repositorio.md).  
  
## Instalacion  

<b>My SEO analyzer</b> no necesita instalación y se ejecuta igual que cualquier otro script de Python.  

> Para ejecutar el script abre una terminal   
> y pásale al intérprete de Python,  
> la ruta al fichero ```__main__.py```  
> que se encuentra en la raíz del repositorio.  

1 - Me ubico en el directorio que contiene el repositorio:  
```cd ~\Downloads\my-seo-analyzer-main```  

2- Si es necesario, renombro el directorio del repositorio:  
```mv my-seo-analyzer-main my-seo-analyzer```  

3- Ejecuto el script  
```python my-seo-analyzer```  

## Ejemplos de uso   
  
Mostrar versión:  
<code> py my-seo-analyzer -v </code>  
<code> py my-seo-analyzer --version </code>  

Mostrar ayuda:  
<code> py my-seo-analyzer -h </code>  
<code> py my-seo-analyzer --help </code> 

Ejemplo de petición HTTP:  
```py my-seo-analyzer -url paginaweb.com```  
```py my-seo-analyzer -url http://paginaweb.com```  

Ejemplo de petición HTTPS:  
```py my-seo-analyzer -url paginaweb.com -https```  
```py my-seo-analyzer -url https://paginaweb.com```  
  
## Compatibilidad  

<b>My SEO analyzer</b> es un script multiplataforma.

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

1. [Description](#description)
2. [Requirements](#requirements)
3. [Dependencies](#dependencies)
5. [Installation](#installation)
6. [Examples of use](#examples-of-use)
7. [Compatibility](#compatibility)

</div>

<div id="readme-en">

## Description
Is an interactive terminal app wich allows to make a request to a HTML, analyze SEO of the HTTP response and generate a report in PDF format.  

- The HTTP headers of the response
- The meta tags
- The titles
- The DOM of the HTML document
- The text content
- The links 
  
## Requirements

<b>My SEO analyzer</b> is wrote with [Python 3](https://www.python.org/downloads/), so requires to have intalled [Python 3](https://www.python.org/downloads/) language and [Pip]().
  
## Dependencies

<b>My SEO analyzer</b> depends on the following Python thirth party libraries:  

- [Requests](https://requests.readthedocs.io/en/latest/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [lxml](https://lxml.de/index.html#documentation)
- [ReportLab]()

> Install with Pip all the dependencies from requirements.txt  
````pip install -r requirements.txt````  
  
## Installation
<b>My SEO analyzer</b> doesn't need installation.  

> To run the script, open a terminal 
> and give to the Python interpreter,  
> the path to the ```__main__.py``` file.   

1 - Go to the repository directory:  
```cd ~\Downloads\my-seo-analyzer-main```  

If is neccesary, rename the directory of the repository:  
```mv my-seo-analyzer-main my-seo-analyzer```  

3- Run el script  
```python my-seo-analyzer```  

## Examples of use

<b>My SEO analyzer</b> runs like any other Python 3 script.   

<b>Show version:</b>  
````python my-seo-analyzer -v````  
or  
````python my-seo-analyzer --version````  

<b>Show help:</b>  
````python my-seo-analyzer -h````  
or  
````python my-seo-analyzer --help````  

<b>HTTP request example:</b>  
````python my-seo-analyzer -url webpage.com````  

<b>HTTPS request example:</b>  
````python my-seo-analyzer -url webpage.com -https````  
  
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
