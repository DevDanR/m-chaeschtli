export interface Product {
  id?: string;
  name?: string;
  keepability?: number;
  category?: string;
  image?: Image;
  m_check2?: any
}

export interface Image {
  original?: string
}

export interface MCheck {
  carbon_footprint?: string
}

