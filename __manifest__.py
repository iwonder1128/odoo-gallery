{
    "name": "Gallery",
    "version": "18.0.1.0.0",
    "author": "APEX",
    "website": "https://apexmech.org",
    #"maintainers": ["florian-dacosta", "sebastienbeau", "GSLabIt", "bealdav"],
    "license": "AGPL-3",
    "category": "Generic Modules",
    "depends": [
        "attachment_queue",
        "fs_storage",  # https://github.com/OCA/storage
    ],
    "data": [
        "views/attachment_queue_views.xml",
        "views/attachment_synchronize_task_views.xml",
        "views/storage_backend_views.xml",
        "data/cron.xml",
        "security/ir.model.access.csv",
    ],
    "demo": ["demo/attachment_synchronize_task_demo.xml"],
    "installable": True,
    "development_status": "Beta",
}
