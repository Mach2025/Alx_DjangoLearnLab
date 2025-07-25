# LibraryProject
# Permissions and Groups Setup
Custom Permissions (defined in `Product` model):
- `can_view`: View product list/details
- `can_create`: Add new product
- `can_edit`: Edit existing product
- `can_delete`: Delete product

## User Groups:
- `Viewers`: Assigned `can_view` permission only.
- `Editors`: Assigned `can_view`, `can_create`, and `can_edit`.
- `Admins`: Assigned all permissions.

## Views:
Each view checks permissions using `@permission_required`:
- `product_list` → `can_view`
- `product_create` → `can_create`
- `product_edit` → `can_edit`
- `product_delete` → `can_delete`