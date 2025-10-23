from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos de datos
class Seccion(BaseModel):
    titulo: str
    contenido: str
    puntos_clave: List[str]
    nivel: int

class Flashcard(BaseModel):
    id: int
    pregunta: str
    respuesta: str
    categoria: str
    dificultad: str

# Datos del temario
temario = [
    {
        "titulo": "1. Introducción a la Programación",
        "contenido": """La programación es el proceso de crear software mediante lenguajes de programación. 
        
        **Conceptos fundamentales:**
        - **Algoritmo**: Serie de pasos ordenados para resolver un problema
        - **Programa**: Algoritmo escrito en un lenguaje de programación
        - **Abstracción**: Dividir problemas grandes en problemas más pequeños
        - **Modularidad**: Estructurar el código en módulos independientes
        
        El desarrollo de software sigue estas fases:
        1. Análisis del problema
        2. Diseño del algoritmo
        3. Codificación
        4. Pruebas y depuración
        5. Mantenimiento""",
        "puntos_clave": [
            "Un algoritmo debe ser preciso, bien definido y finito",
            "El pseudocódigo es independiente del lenguaje de programación",
            "Divide y vencerás es una estrategia clave en programación",
            "La documentación es fundamental para mantener el código"
        ],
        "nivel": 1
    },
    {
        "titulo": "2. Fases de la Programación",
        "contenido": """El proceso de desarrollo de software se divide en tres fases principales:
        
        **Fase 1: Resolución del Problema**
        - Análisis: Definir entradas y salidas esperadas
        - Diseño: Crear el algoritmo que resuelve el problema
        - Validación: Probar el algoritmo con datos de prueba
        
        **Fase 2: Implementación**
        - Codificación: Escribir el código en un lenguaje de programación
        - Compilación: Traducir el código fuente a código ejecutable
        - Pruebas: Verificar que el programa funciona correctamente
        - Documentación: Crear manuales y comentarios
        
        **Fase 3: Explotación y Mantenimiento**
        - Instalación: Poner el programa en producción
        - Mantenimiento: Corregir errores y añadir mejoras
        - Evaluación: Revisar el rendimiento del software""",
        "puntos_clave": [
            "El análisis determina QUÉ debe hacer el programa",
            "El diseño determina CÓMO lo hará",
            "Las pruebas deben hacerse ANTES de la entrega",
            "El mantenimiento es una fase continua"
        ],
        "nivel": 1
    },
    {
        "titulo": "3. Lenguajes de Programación",
        "contenido": """Los lenguajes de programación se clasifican por su nivel de abstracción:
        
        **Lenguaje Máquina (Nivel más bajo)**
        - Código binario (0s y 1s)
        - Directamente ejecutable por el procesador
        - Muy difícil de leer y escribir
        
        **Lenguaje Ensamblador**
        - Usa mnemotécnicos (MOV, ADD, SUB)
        - Dependiente del hardware
        - Más legible que el lenguaje máquina
        
        **Lenguajes de Alto Nivel**
        - Similares al lenguaje humano (Java, Python, C++)
        - Independientes del hardware
        - Requieren compilación o interpretación
        
        **Compilados vs Interpretados:**
        - Compilados: El código se traduce completamente antes de ejecutarse (C, C++)
        - Interpretados: El código se traduce línea por línea durante la ejecución (Python, JavaScript)
        - Java es híbrido: se compila a bytecode y luego se interpreta en la JVM""",
        "puntos_clave": [
            "Lenguaje máquina: solo 0s y 1s",
            "Ensamblador: dependiente del hardware",
            "Alto nivel: independiente del hardware",
            "Java es compilado E interpretado"
        ],
        "nivel": 1
    },
    {
        "titulo": "4. El Lenguaje Java - Historia y Características",
        "contenido": """Java fue creado por Sun Microsystems en 1995 (ahora propiedad de Oracle).
        
        **Características principales:**
        - **Orientado a Objetos**: Todo en Java es un objeto
        - **Independiente de plataforma**: 'Write Once, Run Everywhere'
        - **Robusto**: Gestión automática de memoria (Garbage Collector)
        - **Seguro**: Control de acceso y verificación de bytecode
        - **Simple**: Sintaxis similar a C++, pero más sencilla
        
        **Componentes de Java:**
        - JDK (Java Development Kit): Herramientas de desarrollo
        - JRE (Java Runtime Environment): Entorno de ejecución
        - JVM (Java Virtual Machine): Máquina virtual que ejecuta bytecode
        
        **Ediciones de Java:**
        - Java SE: Aplicaciones de escritorio
        - Java EE: Aplicaciones empresariales
        - Java ME: Dispositivos móviles""",
        "puntos_clave": [
            "Java es independiente de la plataforma gracias a la JVM",
            "El Garbage Collector libera memoria automáticamente",
            "Java compila a bytecode, no a código máquina",
            "'Write Once, Run Everywhere' es el lema de Java"
        ],
        "nivel": 1
    },
    {
        "titulo": "5. Variables e Identificadores en Java",
        "contenido": """Las variables son espacios en memoria que almacenan datos.
        
        **Reglas para identificadores:**
        - Pueden contener letras, dígitos, '_' y '$'
        - NO pueden empezar con dígito
        - Java distingue mayúsculas de minúsculas
        - NO se pueden usar palabras reservadas (int, class, if, etc.)
        
        **Convenciones de nomenclatura:**
        - Variables y métodos: camelCase (miVariable)
        - Constantes: MAYUSCULAS_CON_GUION (MAX_VALOR)
        - Clases: PascalCase (MiClase)
        
        **Declaración de variables:**
        ```java
        int edad = 25;           // Variable entera
        double precio = 19.99;   // Variable decimal
        String nombre = 'Juan';  // Cadena de texto
        final double PI = 3.1416; // Constante
        ```
        
        **Tipos de variables:**
        - Variables mutables: su valor puede cambiar
        - Variables inmutables (constantes): se declaran con 'final'""",
        "puntos_clave": [
            "Java diferencia mayúsculas de minúsculas",
            "Las constantes se declaran con 'final'",
            "camelCase para variables, MAYUSCULAS para constantes",
            "Los identificadores no pueden empezar con número"
        ],
        "nivel": 2
    },
    {
        "titulo": "6. Tipos de Datos Primitivos",
        "contenido": """Java tiene 8 tipos de datos primitivos:
        
        **Enteros:**
        - byte (8 bits): -128 a 127
        - short (16 bits): -32,768 a 32,767
        - int (32 bits): -2,147,483,648 a 2,147,483,647
        - long (64 bits): muy grandes (añadir 'L' al final)
        
        **Decimales:**
        - float (32 bits): precisión simple (añadir 'f')
        - double (64 bits): precisión doble (por defecto)
        
        **Otros:**
        - boolean: true o false
        - char: un solo carácter Unicode (entre comillas simples)
        
        **Ejemplos:**
        ```java
        int edad = 30;
        double salario = 1500.50;
        boolean activo = true;
        char inicial = 'J';
        long poblacion = 7000000000L;
        float temperatura = 36.5f;
        ```
        
        **Tipos Referenciados:**
        - String: cadena de caracteres
        - Arrays: colecciones de elementos
        - Objetos: instancias de clases""",
        "puntos_clave": [
            "int es el tipo entero más usado",
            "double es el tipo decimal por defecto",
            "boolean solo tiene true/false",
            "char usa comillas simples, String usa dobles"
        ],
        "nivel": 2
    },
    {
        "titulo": "7. Operadores en Java",
        "contenido": """Los operadores permiten realizar operaciones sobre datos.
        
        **Operadores Aritméticos:**
        - Suma: +
        - Resta: -
        - Multiplicación: *
        - División: /
        - Módulo (resto): %
        - Incremento: ++
        - Decremento: --
        
        **Operadores de Asignación:**
        - Asignación: =
        - Combinados: +=, -=, *=, /=, %=
        
        **Operadores Relacionales:**
        - Igual a: ==
        - Distinto de: !=
        - Mayor que: >
        - Menor que: <
        - Mayor o igual: >=
        - Menor o igual: <=
        
        **Operadores Lógicos:**
        - AND: && (y lógico)
        - OR: || (o lógico)
        - NOT: ! (negación)
        
        **Operador Condicional (ternario):**
        ```java
        resultado = (condicion) ? valorSiTrue : valorSiFalse;
        ```
        
        **Ejemplos:**
        ```java
        int x = 10, y = 5;
        int suma = x + y;        // 15
        boolean esMayor = x > y; // true
        String msg = (x > y) ? 'Mayor' : 'Menor'; // 'Mayor'
        ```""",
        "puntos_clave": [
            "% devuelve el resto de una división",
            "== compara valores, = asigna valores",
            "&& y || son operadores lógicos",
            "El operador ternario ?: es muy útil para asignaciones condicionales"
        ],
        "nivel": 2
    },
    {
        "titulo": "8. Precedencia de Operadores",
        "contenido": """La precedencia determina el orden en que se evalúan los operadores.
        
        **Orden de precedencia (de mayor a menor):**
        1. Paréntesis: ()
        2. Unarios: ++, --, !, ~
        3. Multiplicativos: *, /, %
        4. Aditivos: +, -
        5. Relacionales: <, >, <=, >=
        6. Igualdad: ==, !=
        7. Lógico AND: &&
        8. Lógico OR: ||
        9. Condicional: ?:
        10. Asignación: =, +=, -=, etc.
        
        **Ejemplos:**
        ```java
        int resultado = 10 + 5 * 2;      // 20 (no 30)
        int resultado2 = (10 + 5) * 2;   // 30
        boolean b = 5 > 3 && 2 < 4;      // true
        ```
        
        **Regla de oro:**
        Usa paréntesis cuando tengas dudas sobre la precedencia. Hace el código más legible.""",
        "puntos_clave": [
            "La multiplicación y división se evalúan antes que suma y resta",
            "Los paréntesis tienen la mayor precedencia",
            "Los operadores del mismo nivel se evalúan de izquierda a derecha",
            "Usar paréntesis mejora la legibilidad"
        ],
        "nivel": 2
    },
    {
        "titulo": "9. Conversión de Tipos (Casting)",
        "contenido": """La conversión de tipos permite cambiar un dato de un tipo a otro.
        
        **Conversión Implícita (Automática):**
        Se hace automáticamente cuando no hay pérdida de información:
        ```java
        int entero = 10;
        double decimal = entero;  // OK: 10.0
        ```
        
        **Conversión Explícita (Casting):**
        Se debe indicar explícitamente cuando puede haber pérdida de datos:
        ```java
        double decimal = 10.99;
        int entero = (int) decimal;  // 10 (se pierde .99)
        ```
        
        **Reglas de promoción:**
        - byte → short → int → long → float → double
        - Si mezclas tipos, el resultado será del tipo mayor
        
        **Conversiones con String:**
        ```java
        // String a número
        int num = Integer.parseInt('123');
        double d = Double.parseDouble('12.34');
        
        // Número a String
        String s = String.valueOf(123);
        String s2 = '' + 123;  // Concatenación
        ```""",
        "puntos_clave": [
            "Casting explícito: (tipo)variable",
            "int a double es automático, double a int requiere casting",
            "Al convertir float/double a int se pierde la parte decimal",
            "Integer.parseInt() convierte String a int"
        ],
        "nivel": 2
    },
    {
        "titulo": "10. Estructura de un Programa Java",
        "contenido": """Todo programa Java tiene una estructura básica:
        
        **Estructura mínima:**
        ```java
        public class MiPrograma {
            public static void main(String[] args) {
                // Código del programa
                System.out.println('¡Hola Mundo!');
            }
        }
        ```
        
        **Componentes:**
        - **Clase principal**: Contiene el método main
        - **Método main**: Punto de entrada del programa
        - **Comentarios**: // para una línea, /* */ para varias
        - **Punto y coma**: Termina cada instrucción
        - **Llaves {}**: Delimitan bloques de código
        
        **Buenas prácticas:**
        - El nombre del archivo debe coincidir con el nombre de la clase pública
        - Un archivo .java puede tener varias clases, pero solo una pública
        - Indentar correctamente el código
        - Usar nombres descriptivos
        
        **Compilación y ejecución:**
        ```
        javac MiPrograma.java    // Compila
        java MiPrograma           // Ejecuta
        ```""",
        "puntos_clave": [
            "main es el punto de entrada del programa",
            "El nombre del archivo debe coincidir con la clase pública",
            "Java distingue entre mayúsculas y minúsculas",
            "System.out.println() muestra texto en consola"
        ],
        "nivel": 1
    },
    {
        "titulo": "11. Entrada y Salida de Datos",
        "contenido": """**Salida de datos (println):**
        ```java
        System.out.println('Hola');  // Con salto de línea
        System.out.print('Hola');    // Sin salto de línea
        System.out.printf('Edad: %d', 25); // Con formato
        ```
        
        **Entrada de datos (Scanner):**
        ```java
        import java.util.Scanner;
        
        Scanner teclado = new Scanner(System.in);
        
        System.out.print('Introduce tu nombre: ');
        String nombre = teclado.nextLine();
        
        System.out.print('Introduce tu edad: ');
        int edad = teclado.nextInt();
        
        System.out.print('Introduce tu altura: ');
        double altura = teclado.nextDouble();
        ```
        
        **Métodos de Scanner:**
        - nextInt(): lee un entero
        - nextDouble(): lee un decimal
        - nextLine(): lee una línea completa
        - next(): lee una palabra
        - nextBoolean(): lee true/false""",
        "puntos_clave": [
            "println añade salto de línea, print no",
            "Scanner permite leer datos del teclado",
            "Hay que importar java.util.Scanner",
            "nextLine() lee toda la línea hasta Enter"
        ],
        "nivel": 2
    },
    {
        "titulo": "12. Trabajo con Cadenas (String)",
        "contenido": """String es una clase especial en Java para trabajar con texto.
        
        **Creación de Strings:**
        ```java
        String s1 = 'Hola';              // Forma simple
        String s2 = new String('Hola'); // Con constructor
        ```
        
        **Métodos importantes:**
        ```java
        String texto = 'Hola Mundo';
        
        texto.length()           // 10 (longitud)
        texto.charAt(0)          // 'H' (carácter en posición)
        texto.substring(0, 4)    // 'Hola' (subcadena)
        texto.toUpperCase()      // 'HOLA MUNDO'
        texto.toLowerCase()      // 'hola mundo'
        texto.equals('Hola')     // false (comparación)
        texto.contains('Mundo')  // true (contiene)
        texto.replace('o', 'a')  // 'Hala Munda'
        ```
        
        **Concatenación:**
        ```java
        String nombre = 'Juan';
        String saludo = 'Hola ' + nombre;  // 'Hola Juan'
        String edad = 'Tengo ' + 25 + ' años';
        ```
        
        **IMPORTANTE:**
        - Para comparar Strings usa .equals(), NO ==
        - Los Strings son inmutables (no se pueden modificar)""",
        "puntos_clave": [
            "Usa .equals() para comparar Strings, NO ==",
            "length() devuelve la longitud",
            "Los índices empiezan en 0",
            "+ concatena Strings"
        ],
        "nivel": 2
    },
    {
        "titulo": "13. Entornos de Desarrollo (IDEs)",
        "contenido": """Un IDE es un programa que facilita el desarrollo de software.
        
        **IDEs populares para Java:**
        - **NetBeans**: IDE oficial de Oracle, fácil de usar
        - **Eclipse**: Muy potente y extensible
        - **IntelliJ IDEA**: Popular y profesional
        - **Visual Studio Code**: Ligero con extensiones Java
        
        **Ventajas de usar un IDE:**
        - Autocompletado de código
        - Detección de errores en tiempo real
        - Depuración integrada
        - Refactorización automática
        - Gestión de proyectos
        - Integración con control de versiones
        
        **NetBeans:**
        - Gratuito y open source
        - Incluye todas las herramientas necesarias
        - Fácil de instalar y configurar
        - Excelente para principiantes
        
        **Sin IDE:**
        También puedes programar con:
        - Editor de texto (Notepad++, Sublime)
        - Compilar: javac MiPrograma.java
        - Ejecutar: java MiPrograma""",
        "puntos_clave": [
            "Un IDE facilita mucho el desarrollo",
            "NetBeans es ideal para principiantes",
            "Los IDEs detectan errores antes de compilar",
            "Puedes programar sin IDE, pero es más difícil"
        ],
        "nivel": 1
    },
    {
        "titulo": "14. Ciclo de Vida del Software",
        "contenido": """El software pasa por diferentes etapas desde su creación hasta su fin.
        
        **Fases del ciclo de vida:**
        
        1. **Especificación y Análisis de Requisitos**
           - Reuniones con el cliente
           - Documentar lo que el software debe hacer
           - Crear prototipos
        
        2. **Diseño**
           - Arquitectura del sistema
           - Diseño de interfaces
           - Diagramas UML
        
        3. **Codificación/Implementación**
           - Escribir el código
           - Seguir estándares de codificación
           - Documentar el código
        
        4. **Pruebas**
           - Pruebas unitarias
           - Pruebas de integración
           - Pruebas de sistema
           - Corrección de bugs
        
        5. **Instalación y Paso a Producción**
           - Despliegue en el entorno del cliente
           - Capacitación de usuarios
        
        6. **Mantenimiento**
           - Correctivo: corregir errores
           - Adaptativo: nuevas funcionalidades
           - Perfectivo: mejoras de rendimiento
           - Preventivo: anticiparse a problemas""",
        "puntos_clave": [
            "El mantenimiento es la fase más larga",
            "Las pruebas deben hacerse en cada fase",
            "La documentación es continua",
            "El análisis define QUÉ, el diseño define CÓMO"
        ],
        "nivel": 1
    },
    {
        "titulo": "15. Conceptos Clave - Repaso General",
        "contenido": """**Conceptos fundamentales que debes dominar:**
        
        **Algoritmo vs Programa:**
        - Algoritmo: Solución general e independiente del lenguaje
        - Programa: Algoritmo implementado en un lenguaje específico
        
        **Compilación en Java:**
        1. Código fuente (.java)
        2. Compilador (javac)
        3. Bytecode (.class)
        4. JVM interpreta el bytecode
        5. Código máquina específico
        
        **Programación Orientada a Objetos:**
        - Clase: Plantilla o molde
        - Objeto: Instancia de una clase
        - Encapsulación: Ocultar detalles internos
        - Herencia: Reutilizar código
        - Polimorfismo: Diferentes comportamientos
        
        **Buenas prácticas:**
        - Código limpio y legible
        - Nombres descriptivos
        - Comentarios útiles (no obvios)
        - Indentar correctamente
        - Probar frecuentemente
        - Control de versiones (Git)
        
        **Errores comunes de principiantes:**
        - Olvidar punto y coma ;
        - Confundir = con ==
        - No cerrar llaves {}
        - Mayúsculas/minúsculas incorrectas
        - No inicializar variables""",
        "puntos_clave": [
            "Java compila a bytecode, no a código máquina",
            "La JVM hace Java independiente de plataforma",
            "POO se basa en clases y objetos",
            "El código limpio es tan importante como que funcione"
        ],
        "nivel": 1
    }
]

# Flashcards
flashcards = [
    {
        "id": 1,
        "pregunta": "¿Qué es un algoritmo?",
        "respuesta": "Un algoritmo es una secuencia ordenada de pasos, sin ambigüedades, que conducen a la solución de un problema. Debe ser preciso, bien definido y finito.",
        "categoria": "Conceptos Básicos",
        "dificultad": "Fácil"
    },
    {
        "id": 2,
        "pregunta": "¿Cuáles son las tres características principales de un algoritmo?",
        "respuesta": "1) Debe ser PRECISO (indicar orden de pasos), 2) Debe estar BIEN DEFINIDO (mismo resultado cada vez), 3) Debe ser FINITO (número finito de pasos).",
        "categoria": "Conceptos Básicos",
        "dificultad": "Media"
    },
    {
        "id": 3,
        "pregunta": "¿Qué significa 'Write Once, Run Everywhere' en Java?",
        "respuesta": "Es el lema de Java que significa que el código se escribe una vez y puede ejecutarse en cualquier plataforma que tenga una JVM (Java Virtual Machine), gracias a la independencia de plataforma.",
        "categoria": "Java",
        "dificultad": "Media"
    },
    {
        "id": 4,
        "pregunta": "¿Qué es el bytecode en Java?",
        "respuesta": "El bytecode es un código intermedio (archivos .class) generado por el compilador de Java. No es código máquina específico, sino instrucciones que la JVM puede interpretar y ejecutar en cualquier plataforma.",
        "categoria": "Java",
        "dificultad": "Media"
    },
    {
        "id": 5,
        "pregunta": "¿Cuál es la diferencia entre JDK, JRE y JVM?",
        "respuesta": "JDK (Java Development Kit): herramientas de desarrollo. JRE (Java Runtime Environment): entorno de ejecución que incluye la JVM y bibliotecas. JVM (Java Virtual Machine): máquina virtual que ejecuta el bytecode.",
        "categoria": "Java",
        "dificultad": "Difícil"
    },
    {
        "id": 6,
        "pregunta": "¿Qué palabras NO se pueden usar como identificadores en Java?",
        "respuesta": "Las palabras reservadas del lenguaje (como int, class, public, if, while, etc.) y los literales booleanos true, false y null no se pueden usar como identificadores.",
        "categoria": "Variables",
        "dificultad": "Fácil"
    },
    {
        "id": 7,
        "pregunta": "¿Cómo se declara una constante en Java?",
        "respuesta": "Se declara usando la palabra reservada 'final' antes del tipo de dato. Ejemplo: final double PI = 3.1416; Por convención, los nombres de constantes se escriben en MAYÚSCULAS.",
        "categoria": "Variables",
        "dificultad": "Fácil"
    },
    {
        "id": 8,
        "pregunta": "¿Cuáles son los 8 tipos de datos primitivos en Java?",
        "respuesta": "Enteros: byte, short, int, long. Decimales: float, double. Otros: boolean, char.",
        "categoria": "Tipos de Datos",
        "dificultad": "Media"
    },
    {
        "id": 9,
        "pregunta": "¿Cuál es la diferencia entre int y long?",
        "respuesta": "int usa 32 bits (rango: -2,147,483,648 a 2,147,483,647). long usa 64 bits (rango mucho mayor). Para literales long se añade 'L' al final: 7000000000L",
        "categoria": "Tipos de Datos",
        "dificultad": "Media"
    },
    {
        "id": 10,
        "pregunta": "¿Por qué float y double no son exactos?",
        "respuesta": "Porque representan números en coma flotante con precisión limitada. No pueden almacenar infinitos decimales. float tiene 32 bits (menos preciso), double tiene 64 bits (más preciso).",
        "categoria": "Tipos de Datos",
        "dificultad": "Difícil"
    },
    {
        "id": 11,
        "pregunta": "¿Cuál es la diferencia entre = y == ?",
        "respuesta": "= es el operador de ASIGNACIÓN (asigna un valor a una variable). == es el operador de COMPARACIÓN (compara si dos valores son iguales, devuelve true/false).",
        "categoria": "Operadores",
        "dificultad": "Fácil"
    },
    {
        "id": 12,
        "pregunta": "¿Qué hace el operador % (módulo)?",
        "respuesta": "Devuelve el RESTO de una división entera. Ejemplo: 10 % 3 = 1 (porque 10 entre 3 es 3 y sobra 1). Es útil para saber si un número es par (x % 2 == 0) o impar.",
        "categoria": "Operadores",
        "dificultad": "Media"
    },
    {
        "id": 13,
        "pregunta": "¿Qué es el operador ternario en Java?",
        "respuesta": "Es el operador ?: que evalúa una condición y devuelve un valor u otro. Sintaxis: (condicion) ? valorSiTrue : valorSiFalse. Ejemplo: String resultado = (edad >= 18) ? 'Mayor' : 'Menor';",
        "categoria": "Operadores",
        "dificultad": "Media"
    },
    {
        "id": 14,
        "pregunta": "¿Cuál es la precedencia: 10 + 5 * 2?",
        "respuesta": "El resultado es 20 (no 30), porque la multiplicación (*) tiene mayor precedencia que la suma (+). Primero se calcula 5 * 2 = 10, luego 10 + 10 = 20.",
        "categoria": "Operadores",
        "dificultad": "Media"
    },
    {
        "id": 15,
        "pregunta": "¿Cómo se comparan dos Strings correctamente?",
        "respuesta": "Usando el método .equals() o .equalsIgnoreCase(). NUNCA usar ==. Ejemplo correcto: texto1.equals(texto2). El operador == compara referencias, no contenido.",
        "categoria": "Strings",
        "dificultad": "Fácil"
    },
    {
        "id": 16,
        "pregunta": "¿Cómo se obtiene la longitud de un String?",
        "respuesta": "Usando el método .length(). Ejemplo: String texto = 'Hola'; int longitud = texto.length(); // longitud = 4",
        "categoria": "Strings",
        "dificultad": "Fácil"
    },
    {
        "id": 17,
        "pregunta": "¿Qué es el casting de tipos?",
        "respuesta": "Es la conversión explícita de un tipo de dato a otro. Se usa cuando hay posible pérdida de información. Sintaxis: (tipo)variable. Ejemplo: double d = 10.99; int i = (int)d; // i = 10",
        "categoria": "Conversión de Tipos",
        "dificultad": "Media"
    },
    {
        "id": 18,
        "pregunta": "¿Cuándo se hace conversión automática de tipos?",
        "respuesta": "Cuando se asigna un tipo más pequeño a uno más grande (no hay pérdida de datos). Ejemplo: int x = 10; double y = x; // Automático. La secuencia es: byte → short → int → long → float → double",
        "categoria": "Conversión de Tipos",
        "dificultad": "Media"
    },
    {
        "id": 19,
        "pregunta": "¿Qué es el Garbage Collector?",
        "respuesta": "Es un mecanismo automático de Java que libera la memoria de objetos que ya no se usan. El programador no necesita liberar memoria manualmente como en C/C++.",
        "categoria": "Java",
        "dificultad": "Media"
    },
    {
        "id": 20,
        "pregunta": "¿Cuál es la estructura mínima de un programa Java?",
        "respuesta": "public class NombreClase { public static void main(String[] args) { // código } }. El método main es el punto de entrada obligatorio.",
        "categoria": "Estructura",
        "dificultad": "Fácil"
    },
    {
        "id": 21,
        "pregunta": "¿Cómo se lee un número entero del teclado?",
        "respuesta": "Usando Scanner: import java.util.Scanner; Scanner teclado = new Scanner(System.in); int numero = teclado.nextInt();",
        "categoria": "Entrada/Salida",
        "dificultad": "Media"
    },
    {
        "id": 22,
        "pregunta": "¿Cuál es la diferencia entre print y println?",
        "respuesta": "print() muestra texto SIN salto de línea al final. println() muestra texto CON salto de línea al final. Ejemplo: System.out.println('Hola') añade salto de línea.",
        "categoria": "Entrada/Salida",
        "dificultad": "Fácil"
    },
    {
        "id": 23,
        "pregunta": "¿Qué son las tres fases principales del desarrollo de software?",
        "respuesta": "1) Resolución del problema (análisis y diseño), 2) Implementación (codificación y pruebas), 3) Explotación y mantenimiento.",
        "categoria": "Proceso de Desarrollo",
        "dificultad": "Media"
    },
    {
        "id": 24,
        "pregunta": "¿Qué es la POO (Programación Orientada a Objetos)?",
        "respuesta": "Es un paradigma de programación basado en objetos que tienen propiedades (atributos) y comportamientos (métodos). Principios: Encapsulación, Herencia, Polimorfismo.",
        "categoria": "POO",
        "dificultad": "Media"
    },
    {
        "id": 25,
        "pregunta": "¿Qué es la diferencia entre clase y objeto?",
        "respuesta": "Una CLASE es una plantilla o molde que define las características. Un OBJETO es una instancia concreta de esa clase. Ejemplo: 'Coche' es una clase, 'Mi coche rojo' es un objeto.",
        "categoria": "POO",
        "dificultad": "Media"
    },
    {
        "id": 26,
        "pregunta": "¿Por qué Java es independiente de la plataforma?",
        "respuesta": "Porque el código Java se compila a bytecode (no a código máquina específico) y la JVM de cada plataforma interpreta ese bytecode. El mismo .class funciona en Windows, Linux, Mac, etc.",
        "categoria": "Java",
        "dificultad": "Difícil"
    },
    {
        "id": 27,
        "pregunta": "¿Qué diferencia hay entre lenguaje compilado e interpretado?",
        "respuesta": "COMPILADO: Se traduce todo el código antes de ejecutar (C, C++). INTERPRETADO: Se traduce línea por línea durante la ejecución (Python). Java es híbrido: compila a bytecode y la JVM lo interpreta.",
        "categoria": "Lenguajes",
        "dificultad": "Difícil"
    },
    {
        "id": 28,
        "pregunta": "¿Qué es un IDE y para qué sirve?",
        "respuesta": "IDE (Integrated Development Environment) es un entorno de desarrollo integrado. Facilita escribir código con autocompletado, detección de errores, depuración, compilación integrada, etc. Ejemplos: NetBeans, Eclipse, IntelliJ.",
        "categoria": "Herramientas",
        "dificultad": "Fácil"
    },
    {
        "id": 29,
        "pregunta": "¿Qué son los operadores && y || ?",
        "respuesta": "&& es AND lógico (y): devuelve true si AMBAS condiciones son true. || es OR lógico (o): devuelve true si AL MENOS UNA condición es true. Ejemplo: (x > 5 && x < 10) verifica si x está entre 5 y 10.",
        "categoria": "Operadores",
        "dificultad": "Media"
    },
    {
        "id": 30,
        "pregunta": "¿Cómo se convierte un String a número?",
        "respuesta": "Usando los métodos parse: Integer.parseInt('123') para int, Double.parseDouble('12.34') para double, Long.parseLong('1000') para long, etc.",
        "categoria": "Conversión de Tipos",
        "dificultad": "Media"
    }
]

# Endpoints
@app.get("/")
def root():
    return {"message": "API de Estudio de Programación Java"}

@app.get("/api/temario")
def get_temario():
    """Obtiene todo el temario organizado"""
    return {"temario": temario, "total_secciones": len(temario)}

@app.get("/api/temario/{seccion_id}")
def get_seccion(seccion_id: int):
    """Obtiene una sección específica del temario"""
    if 0 <= seccion_id < len(temario):
        return temario[seccion_id]
    raise HTTPException(status_code=404, detail="Sección no encontrada")

@app.get("/api/flashcards")
def get_flashcards(categoria: Optional[str] = None, dificultad: Optional[str] = None):
    """Obtiene todas las flashcards, opcionalmente filtradas"""
    resultado = flashcards
    
    if categoria:
        resultado = [f for f in resultado if f["categoria"].lower() == categoria.lower()]
    
    if dificultad:
        resultado = [f for f in resultado if f["dificultad"].lower() == dificultad.lower()]
    
    return {"flashcards": resultado, "total": len(resultado)}

@app.get("/api/flashcards/{flashcard_id}")
def get_flashcard(flashcard_id: int):
    """Obtiene una flashcard específica"""
    flashcard = next((f for f in flashcards if f["id"] == flashcard_id), None)
    if flashcard:
        return flashcard
    raise HTTPException(status_code=404, detail="Flashcard no encontrada")

@app.get("/api/categorias")
def get_categorias():
    """Obtiene todas las categorías disponibles"""
    categorias = list(set(f["categoria"] for f in flashcards))
    return {"categorias": sorted(categorias)}

@app.get("/api/resumen")
def get_resumen():
    """Obtiene un resumen general del temario"""
    return {
        "total_secciones": len(temario),
        "total_flashcards": len(flashcards),
        "categorias": list(set(f["categoria"] for f in flashcards)),
        "niveles": [1, 2],
        "dificultades": ["Fácil", "Media", "Difícil"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)