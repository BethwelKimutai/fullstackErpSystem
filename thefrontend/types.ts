export interface UserDetails {
    id: string;
    username: string;
    email: string;
    is_manager: boolean;
    is_accounting_manager: boolean;
    is_inventory_manager: boolean;
    is_purchase_manager: boolean;
    is_superuser: boolean;
    company_id: string;
}  

export interface User {
  username: string;
  passord: string;
  token: string;
} 

export interface token{
  token: string;
}