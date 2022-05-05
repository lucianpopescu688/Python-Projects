# Python-Projects
College assignments and projects in Python

Assignment 3 - The application manages several two-dimensional points and has the following features:

  - Each point is represented by a "MyPoint" class, identified by the following properties:
    - coord_x given as a number;
    - coord_y given as a number;
    - color given as a string(possible colors: red, green, yellow and magenta)
   
   - "MyPoint" class has the following features:
     1. Get and set the value of all properties for a point;
     2. Provide the string represantion of a point;
    
    - The program manages the points in class "PointRepository" and allows operations such as:
      1. Add a point to the repository;
      2. Get all points;
      3. Get a point at a given index;
      4. Get all points of a given color;
      5. Get all points that are inside a given square (up-left corner and length given);
      6. Get the minimum distance between two points;
      7. Update a point at a given index;
      8. Delete a point by index;
      9. Delete all points that are inside a given square;
      10. Plot all points in a chart (using library matplotlib);
      11. Get all points that are inside a given circle (center of circle, radius given);
      12. Get the number of points of a given color;
      13. Shift all points on the y axis;
      
The application is divided into several files/folders:

- Main_class folder contains the file with the class "MyPoint";
- Secondary_class contains the file with the class "PointRepository";
- Main_menu folder contains the file that runs the aplication and the tests;
- Teste folder contains the tests only for "add a point" feature;
- User_inteface folder contains the console type interface; 


