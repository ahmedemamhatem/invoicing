app_name = "invoicing"
app_title = "Invoicing"
app_publisher = "Ahmed Emam"
app_description = "invoicing"
app_email = "ahmedemamhatem@gmail.com"
app_license = "mit"

# Apps
# ------------------
fixtures = [
    {"doctype": "Custom Field"},
    {"doctype": "Translation"},
    {"doctype": "Property Setter"}
]

# Installation
# ------------
after_install = "invoicing.install.set_workspace_visibility"

# Migration
# ------------
after_migrate = "invoicing.install.set_workspace_visibility"

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "invoicing",
# 		"logo": "/assets/invoicing/logo.png",
# 		"title": "Mini System",
# 		"route": "/invoicing",
# 		"has_permission": "invoicing.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/invoicing/css/invoicing.css"
# app_include_js = "/assets/invoicing/js/invoicing.js"

# include js, css files in header of web template
# web_include_css = "/assets/invoicing/css/invoicing.css"
# web_include_js = "/assets/invoicing/js/invoicing.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "invoicing/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "invoicing/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "invoicing.utils.jinja_methods",
# 	"filters": "invoicing.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "invoicing.install.before_install"
# after_install = "invoicing.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "invoicing.uninstall.before_uninstall"
# after_uninstall = "invoicing.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "invoicing.utils.before_app_install"
# after_app_install = "invoicing.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "invoicing.utils.before_app_uninstall"
# after_app_uninstall = "invoicing.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "invoicing.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"invoicing.tasks.all"
# 	],
# 	"daily": [
# 		"invoicing.tasks.daily"
# 	],
# 	"hourly": [
# 		"invoicing.tasks.hourly"
# 	],
# 	"weekly": [
# 		"invoicing.tasks.weekly"
# 	],
# 	"monthly": [
# 		"invoicing.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "invoicing.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "invoicing.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "invoicing.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["invoicing.utils.before_request"]
# after_request = ["invoicing.utils.after_request"]

# Job Events
# ----------
# before_job = ["invoicing.utils.before_job"]
# after_job = ["invoicing.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"invoicing.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

