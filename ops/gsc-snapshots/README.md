# GSC Decision Snapshots

The daily GitHub Action writes dated, normalized, public-safe Search Console
summaries here. Snapshots contain aggregate and page-level performance,
sitemap status, and URL Inspection results only for checked-in URLs.

Credentials, complete raw query exports, country/device rows, and user data
must never be committed. A new schema/privacy-valid snapshot is run-start
evidence: review it against `ops/seo-roadmap.json`, update decisions when it
changes an evidence gate, and otherwise record a healthy no-op.
