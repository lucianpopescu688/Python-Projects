# Python-Projects
College assignments and projects in Python

Assignment 4 - The application manages several vectors and has the following features: 
  
  - Each vector is represented by a "MyVector" class, identified by the following properties:
    - name_id given as a string/int;
    - colour given as one letter(possible values r, g, b, y and m);
    - type given as a positive integer greater or equalt to 1;
    - values given as a list of numbers;
   
  - "MyVector" class has the following features:
  
     1.Scalar operations: 
      - add a scalar to vector;
     
     2.Vector operations: 
      - add two vectors;
      - subtract two vectos;
      - multiplication;
                          
     3.Reduction operations: 
       - sum of elements in a vector;
       - product of elements in a vectors;
       - average of elements in a vector;
       - minimum of a vector;
       - maximum of a vector;
     
   - The program manages the points in class "VectorRepository" and allows operations such as:
    
        1.Add a vector to the repository;
      
        2.Get all vectors;
      
        3.Get a vector at a given index;
      
        4.Update a vector at a given index;
      
        5.Update a vector identified by 𝑛ame_id;
      
        6.Delete a vector by index;
      
        7.Delete a vector by name_id;
      
        8.Plot all vectors in a char based on the type and colour of each vector(using library matplotlib). Type is interpreted as follows: 1 - circle , 2 - square, 3 - triangle, any other value - diamond;
      
        9.Get the sum of elements in all vectors;
      
        10.Delete all vectors from the repository;
      
        11.Update all vectors having a given type by setting their color to the same given value;
        
The application is divided into several files/folders:

- Domain folder contains the file with the class "MyVector";
- Infrastructure contains the file with the class "VectorRepository";
- Main folder contains the file that runs the aplication;
- User_inteface folder contains the console type interface; 
- Application folder contains the controller class;
- Data_examples folder contains data examples for class "MyVector"(using and not using library numpy) and for class "VectorRepository";
