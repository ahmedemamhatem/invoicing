import frappe

def set_workspace_visibility():
    """
    Sets `is_hidden` to 1 for all Workspaces except "Home" and "Users".
    """
    try:
        # Fetch all workspaces except "Home" and "Users"
        workspaces = frappe.get_all(
            "Workspace",
            filters={"name": ["not in", ["إعدادات الفواتير", "مدير النظام", "العملاء", "الموردين"]]},
            fields=["name", "is_hidden"]
        )
        
        # Update the is_hidden field for the fetched workspaces
        for workspace in workspaces:
            frappe.db.set_value("Workspace", workspace.name, "is_hidden", 1)
        
        # Commit changes to the database
        frappe.db.commit()

        frappe.log("Workspace visibility updated successfully.", "info")
    except Exception as e:
        frappe.log_error(f"Error updating workspace visibility: {str(e)}", "Workspace Visibility Error")