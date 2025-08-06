# securestack-ops-platform

Internal Developer Platform using Backstage, Ansible, Bash, and Python to automate secure app and network provisioning.

## 💡 Use Case

This project simulates how platform engineers support developers with:

- Secure, self-service app provisioning
- Enforced firewall rules and network zones
- DevOps automation and infrastructure-as-code
- Diagnostics and observability

## 📁 Project Structure

```text
securestack-ops-platform/
├── backstage/              # Backstage configuration and plugins
│   ├── app-template/       # Scaffolder templates
│   └── plugins/            # Custom Backstage plugins
├── automation/
│   ├── ansible/            # Playbooks for firewall and system config
│   ├── bash/               # CLI utilities and wrappers
│   └── python/             # Diagnostic and provisioning CLI
├── services/
│   └── hello-app/          # Sample service provisioned through Backstage
├── docs/                   # Diagrams and architecture
├── tests/                  # Unit or integration tests
└── .github/workflows/      # CI/CD pipeline
```

## 🧱 Features

- Self-service application onboarding via Backstage
- Automated firewall provisioning with Ansible
- Python CLI for connectivity tests (e.g., netcheck)
- GitHub Actions CI pipeline for sample services

## 🛠 Tech Stack

- Backstage (Developer Portal)
- Ansible
- Bash
- Python
- GitHub Actions
- Docker (optional for services)
- iptables / firewalld (simulated firewall rules)

## 📚 Documentation

- [`docs/network-diagram.png`](docs/network-diagram.png)
- [`docs/developer-workflows.md`](docs/developer-workflows.md)
