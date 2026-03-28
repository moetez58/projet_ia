export interface Property {
    surface: number;
    chambres: number;
    prix: number;
  }
  
  export interface Stats {
    mean_surface: number;
    mean_prix: number;
    mean_chambres: number;
    correlation: number;
    count: number;
  }
  
  export interface ApiData {
    columns: string[];
    rows: (string | number)[][];
    count: number;
  }