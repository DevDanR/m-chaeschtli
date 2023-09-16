export interface Product {
  id?: string;
  name?: string;
  keepability?: number;
  category?: string;
  image?: Image;
}

export interface Image {
  original?: string
}
