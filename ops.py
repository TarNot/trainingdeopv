import { useState } from "react";

const roadmapData = [
  {
    phase: 1,
    title: "Основы Linux & Командная строка",
    duration: "3–4 недели",
    icon: "🐧",
    color: "#00ff88",
    topics: [
      "Файловая система Linux (ls, cd, mkdir, rm, cp, mv)",
      "Права доступа (chmod, chown, sudo)",
      "Работа с текстом (cat, grep, sed, awk)",
      "Процессы и системные ресурсы (ps, top, kill)",
      "Bash-скрипты: переменные, условия, циклы",
      "SSH: подключение к серверу",
    ],
    tasks: [
      "Установить Ubuntu в VirtualBox или WSL2",
      "Написать bash-скрипт для бекапа папки",
      "Настроить SSH-ключи и подключиться к серверу",
      "Создать cron-задачу для автозапуска скрипта",
    ],
    resources: [
      { name: "OverTheWire: Bandit", url: "https://overthewire.org/wargames/bandit/", type: "Практика" },
      { name: "Linux Journey", url: "https://linuxjourney.com/", type: "Теория" },
      { name: "HackerRank Linux Shell", url: "https://www.hackerrank.com/domains/shell", type: "Упражнения" },
      { name: "Explainshell.com", url: "https://explainshell.com/", type: "Справочник" },
    ],
  },
  {
    phase: 2,
    title: "Сети & Протоколы",
    duration: "2–3 недели",
    icon: "🌐",
    color: "#00cfff",
    topics: [
      "Модель OSI и TCP/IP",
      "IP-адресация, маски подсетей, CIDR",
      "DNS: как работает разрешение имён",
      "HTTP/HTTPS: методы, коды статусов, заголовки",
      "Firewall и базовая безопасность (iptables, ufw)",
      "Инструменты: curl, wget, netstat, ping, traceroute",
    ],
    tasks: [
      "Настроить статический IP на Linux-машине",
      "Поднять простой HTTP-сервер на Python",
      "Исследовать DNS-запросы через dig и nslookup",
      "Настроить базовые правила ufw",
    ],
    resources: [
      { name: "Cisco Networking Basics (Coursera)", url: "https://www.coursera.org/learn/computer-networking", type: "Курс" },
      { name: "Subnetting Practice", url: "https://subnettingpractice.com/", type: "Практика" },
      { name: "HTTP cats", url: "https://http.cat/", type: "Справочник" },
      { name: "TryHackMe Pre-Security", url: "https://tryhackme.com/path/outline/presecurity", type: "Практика" },
    ],
  },
  {
    phase: 3,
    title: "Git & Контроль версий",
    duration: "1–2 недели",
    icon: "🔀",
    color: "#ff6b35",
    topics: [
      "Основы Git: init, add, commit, push, pull",
      "Ветки: branch, merge, rebase",
      "GitHub/GitLab: pull request, code review",
      "Git Flow и стратегии ветвления",
      ".gitignore и работа с удалёнными репозиториями",
      "Разрешение конфликтов",
    ],
    tasks: [
      "Создать репозиторий и опубликовать bash-скрипты из фазы 1",
      "Сделать feature-ветку, внести изменения и создать PR",
      "Сымитировать конфликт и разрешить его",
      "Настроить Git aliases для ускорения работы",
    ],
    resources: [
      { name: "Learn Git Branching", url: "https://learngitbranching.js.org/", type: "Интерактив" },
      { name: "Oh My Git!", url: "https://ohmygit.org/", type: "Игра" },
      { name: "Git Katas", url: "https://github.com/eficode-academy/git-katas", type: "Упражнения" },
      { name: "Atlassian Git Tutorials", url: "https://www.atlassian.com/git/tutorials", type: "Теория" },
    ],
  },
  {
    phase: 4,
    title: "Docker & Контейнеризация",
    duration: "3–4 недели",
    icon: "🐳",
    color: "#2496ed",
    topics: [
      "Что такое контейнеры vs виртуальные машины",
      "Dockerfile: FROM, RUN, COPY, CMD, ENTRYPOINT",
      "Docker-образы: build, push, pull",
      "Docker Compose: многоконтейнерные приложения",
      "Тома (volumes) и сети в Docker",
      "Docker Hub и реестры образов",
    ],
    tasks: [
      "Запустить nginx в Docker-контейнере",
      "Создать Dockerfile для Node.js/Python-приложения",
      "Поднять стек: приложение + база данных через docker-compose",
      "Оптимизировать размер образа с multi-stage builds",
    ],
    resources: [
      { name: "Play with Docker", url: "https://labs.play-with-docker.com/", type: "Практика" },
      { name: "Docker Labs", url: "https://dockerlabs.collabnix.com/", type: "Упражнения" },
      { name: "KodeKloud Docker", url: "https://kodekloud.com/courses/docker-for-the-absolute-beginner/", type: "Курс" },
      { name: "Dive (анализ образов)", url: "https://github.com/wagoodman/dive", type: "Инструмент" },
    ],
  },
  {
    phase: 5,
    title: "CI/CD Pipelines",
    duration: "2–3 недели",
    icon: "⚙️",
    color: "#a855f7",
    topics: [
      "Концепция CI/CD: непрерывная интеграция и доставка",
      "GitHub Actions: workflows, jobs, steps",
      "GitLab CI/CD: .gitlab-ci.yml",
      "Тестирование в pipeline (lint, unit tests)",
      "Сборка и публикация Docker-образов в CI",
      "Секреты и переменные среды в pipeline",
    ],
    tasks: [
      "Настроить GitHub Actions для автолинтинга кода",
      "Создать pipeline: тест → сборка образа → push в Docker Hub",
      "Добавить badge статуса сборки в README",
      "Настроить уведомления о падении pipeline",
    ],
    resources: [
      { name: "GitHub Actions Docs", url: "https://docs.github.com/en/actions", type: "Документация" },
      { name: "GitHub Actions by Example", url: "https://www.actionsbyexample.com/", type: "Примеры" },
      { name: "KodeKloud GitHub Actions", url: "https://kodekloud.com/courses/github-actions/", type: "Курс" },
      { name: "CI/CD with GitLab (FreeCodeCamp)", url: "https://www.freecodecamp.org/news/gitlab-ci-cd-tutorial/", type: "Туториал" },
    ],
  },
  {
    phase: 6,
    title: "Kubernetes (K8s)",
    duration: "4–6 недель",
    icon: "☸️",
    color: "#326ce5",
    topics: [
      "Архитектура K8s: Node, Pod, Cluster",
      "Основные объекты: Pod, Deployment, Service",
      "ConfigMap и Secrets",
      "Ingress и балансировка нагрузки",
      "Persistent Volumes и хранилище",
      "Helm: менеджер пакетов для K8s",
    ],
    tasks: [
      "Развернуть кластер minikube локально",
      "Задеплоить приложение с 3 репликами через Deployment",
      "Настроить rolling update без даунтайма",
      "Установить приложение через Helm chart",
    ],
    resources: [
      { name: "Kubernetes.io Interactive Tutorial", url: "https://kubernetes.io/docs/tutorials/", type: "Туториал" },
      { name: "KillerCoda K8s", url: "https://killercoda.com/playgrounds/scenario/kubernetes", type: "Практика" },
      { name: "KodeKloud CKA Course", url: "https://kodekloud.com/courses/certified-kubernetes-administrator-cka/", type: "Курс" },
      { name: "Killer.sh (симулятор экзамена)", url: "https://killer.sh/", type: "Экзамен" },
    ],
  },
  {
    phase: 7,
    title: "Cloud: AWS / GCP / Azure",
    duration: "4–6 недель",
    icon: "☁️",
    color: "#ff9900",
    topics: [
      "Основные сервисы: EC2/Compute, S3/Storage, RDS/Database",
      "IAM: управление доступом и политики",
      "VPC: виртуальные сети и подсети",
      "Load Balancer и Auto Scaling",
      "Serverless: Lambda/Cloud Functions",
      "Infrastructure as Code: Terraform основы",
    ],
    tasks: [
      "Создать EC2-инстанс и задеплоить приложение",
      "Настроить S3-бакет со статическим сайтом",
      "Написать Terraform-конфиг для создания инфраструктуры",
      "Пройти AWS Cloud Practitioner Practice Exam",
    ],
    resources: [
      { name: "AWS Free Tier", url: "https://aws.amazon.com/free/", type: "Практика" },
      { name: "A Cloud Guru", url: "https://acloudguru.com/", type: "Курс" },
      { name: "AWS Skill Builder", url: "https://skillbuilder.aws/", type: "Официальный" },
      { name: "Terraform Learn", url: "https://developer.hashicorp.com/terraform/tutorials", type: "Туториал" },
    ],
  },
  {
    phase: 8,
    title: "Мониторинг & Observability",
    duration: "2–3 недели",
    icon: "📊",
    color: "#f59e0b",
    topics: [
      "Prometheus: метрики и alerting",
      "Grafana: дашборды и визуализация",
      "Loki: агрегация логов",
      "Tracing: Jaeger / OpenTelemetry",
      "SLI, SLO, SLA — определения и практика",
      "Incident management и постмортемы",
    ],
    tasks: [
      "Поднять стек Prometheus + Grafana через docker-compose",
      "Настроить алерт при превышении CPU > 80%",
      "Создать дашборд для мониторинга своего приложения",
      "Написать runbook для типичного инцидента",
    ],
    resources: [
      { name: "Prometheus Getting Started", url: "https://prometheus.io/docs/prometheus/latest/getting_started/", type: "Документация" },
      { name: "Grafana Play", url: "https://play.grafana.org/", type: "Песочница" },
      { name: "Google SRE Book (бесплатно)", url: "https://sre.google/sre-book/table-of-contents/", type: "Книга" },
      { name: "KodeKloud Prometheus", url: "https://kodekloud.com/courses/prometheus-certified-associate/", type: "Курс" },
    ],
  },
];

const typeColors = {
  "Практика": "#00ff88",
  "Теория": "#00cfff",
  "Курс": "#a855f7",
  "Упражнения": "#ff6b35",
  "Интерактив": "#f59e0b",
  "Игра": "#ec4899",
  "Справочник": "#94a3b8",
  "Документация": "#64748b",
  "Туториал": "#22d3ee",
  "Официальный": "#ff9900",
  "Инструмент": "#84cc16",
  "Книга": "#c084fc",
  "Экзамен": "#f87171",
  "Песочница": "#34d399",
};

export default function DevOpsRoadmap() {
  const [activePhase, setActivePhase] = useState(null);
  const [completedTasks, setCompletedTasks] = useState({});
  const [completedTopics, setCompletedTopics] = useState({});

  const toggleTask = (phaseIdx, taskIdx) => {
    const key = `${phaseIdx}-${taskIdx}`;
    setCompletedTasks(prev => ({ ...prev, [key]: !prev[key] }));
  };

  const toggleTopic = (phaseIdx, topicIdx) => {
    const key = `${phaseIdx}-${topicIdx}`;
    setCompletedTopics(prev => ({ ...prev, [key]: !prev[key] }));
  };

  const getPhaseProgress = (phaseIdx) => {
    const phase = roadmapData[phaseIdx];
    const totalItems = phase.tasks.length + phase.topics.length;
    const completedCount = phase.tasks.filter((_, i) => completedTasks[`${phaseIdx}-${i}`]).length
      + phase.topics.filter((_, i) => completedTopics[`${phaseIdx}-${i}`]).length;
    return totalItems > 0 ? Math.round((completedCount / totalItems) * 100) : 0;
  };

  const totalProgress = () => {
    let total = 0, completed = 0;
    roadmapData.forEach((phase, pi) => {
      total += phase.tasks.length + phase.topics.length;
      completed += phase.tasks.filter((_, i) => completedTasks[`${pi}-${i}`]).length
        + phase.topics.filter((_, i) => completedTopics[`${pi}-${i}`]).length;
    });
    return total > 0 ? Math.round((completed / total) * 100) : 0;
  };

  const prog = totalProgress();

  return (
    <div style={{
      minHeight: "100vh",
      background: "#0a0e1a",
      color: "#e2e8f0",
      fontFamily: "'JetBrains Mono', 'Fira Code', monospace",
      padding: "0",
    }}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;600;700&family=Syne:wght@700;800&display=swap');
        * { box-sizing: border-box; margin: 0; padding: 0; }
        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-track { background: #0a0e1a; }
        ::-webkit-scrollbar-thumb { background: #00ff88; border-radius: 2px; }
        .phase-card { transition: all 0.3s cubic-bezier(0.4,0,0.2,1); }
        .phase-card:hover { transform: translateX(4px); }
        .resource-link { transition: all 0.2s; text-decoration: none; }
        .resource-link:hover { filter: brightness(1.3); }
        .task-item { transition: all 0.2s; cursor: pointer; }
        .task-item:hover { background: rgba(255,255,255,0.05); }
        .topic-item { transition: all 0.2s; cursor: pointer; }
        .topic-item:hover { background: rgba(255,255,255,0.04); }
        .glow-bar { box-shadow: 0 0 12px currentColor; }
        @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.5} }
        @keyframes fadeIn { from{opacity:0;transform:translateY(10px)} to{opacity:1;transform:translateY(0)} }
        .fade-in { animation: fadeIn 0.35s ease forwards; }
        .terminal-cursor { animation: pulse 1s infinite; }
      `}</style>

      {/* Header */}
      <div style={{
        background: "linear-gradient(135deg, #0d1220 0%, #0a1628 50%, #0d1a12 100%)",
        borderBottom: "1px solid rgba(0,255,136,0.15)",
        padding: "40px 32px 32px",
        position: "sticky", top: 0, zIndex: 100,
        backdropFilter: "blur(20px)",
      }}>
        <div style={{ maxWidth: 900, margin: "0 auto" }}>
          <div style={{ display: "flex", alignItems: "center", gap: 12, marginBottom: 8 }}>
            <span style={{ color: "#00ff88", fontSize: 13, letterSpacing: 3 }}>DEVOPS/CLOUD</span>
            <span style={{ color: "#334155", fontSize: 13 }}>•</span>
            <span style={{ color: "#475569", fontSize: 13 }}>ROADMAP v1.0</span>
            <span className="terminal-cursor" style={{ color: "#00ff88", marginLeft: 4 }}>_</span>
          </div>
          <h1 style={{
            fontFamily: "'Syne', sans-serif",
            fontSize: "clamp(24px, 4vw, 42px)",
            fontWeight: 800,
            color: "#f1f5f9",
            letterSpacing: -1,
            marginBottom: 24,
          }}>
            DevOps & Cloud{" "}
            <span style={{ color: "#00ff88" }}>с нуля</span>
          </h1>

          {/* Global progress */}
          <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
            <div style={{ flex: 1, height: 6, background: "#1e2a3a", borderRadius: 3, overflow: "hidden" }}>
              <div style={{
                height: "100%",
                width: `${prog}%`,
                background: "linear-gradient(90deg, #00ff88, #00cfff)",
                borderRadius: 3,
                transition: "width 0.5s ease",
                boxShadow: "0 0 10px #00ff88",
              }} />
            </div>
            <span style={{ color: "#00ff88", fontSize: 14, fontWeight: 600, minWidth: 48 }}>{prog}%</span>
            <span style={{ color: "#475569", fontSize: 12 }}>общий прогресс</span>
          </div>
        </div>
      </div>

      <div style={{ maxWidth: 900, margin: "0 auto", padding: "32px 24px" }}>

        {/* Phase list */}
        <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
          {roadmapData.map((phase, pi) => {
            const isOpen = activePhase === pi;
            const progress = getPhaseProgress(pi);

            return (
              <div key={pi} className="phase-card" style={{
                border: `1px solid ${isOpen ? phase.color + "55" : "rgba(255,255,255,0.07)"}`,
                borderRadius: 12,
                overflow: "hidden",
                background: isOpen ? `rgba(${parseInt(phase.color.slice(1,3),16)},${parseInt(phase.color.slice(3,5),16)},${parseInt(phase.color.slice(5,7),16)},0.04)` : "#0d1220",
              }}>

                {/* Phase header */}
                <div
                  onClick={() => setActivePhase(isOpen ? null : pi)}
                  style={{
                    padding: "18px 24px",
                    cursor: "pointer",
                    display: "flex",
                    alignItems: "center",
                    gap: 16,
                  }}
                >
                  <div style={{
                    width: 44, height: 44,
                    borderRadius: 10,
                    background: `${phase.color}18`,
                    border: `1px solid ${phase.color}44`,
                    display: "flex", alignItems: "center", justifyContent: "center",
                    fontSize: 20, flexShrink: 0,
                  }}>
                    {phase.icon}
                  </div>

                  <div style={{ flex: 1, minWidth: 0 }}>
                    <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 6 }}>
                      <span style={{ color: phase.color, fontSize: 11, fontWeight: 600, letterSpacing: 2 }}>
                        ФАЗА {phase.phase}
                      </span>
                      <span style={{
                        background: `${phase.color}18`,
                        color: phase.color,
                        border: `1px solid ${phase.color}33`,
                        borderRadius: 4, padding: "1px 8px", fontSize: 10,
                      }}>
                        {phase.duration}
                      </span>
                      {progress === 100 && (
                        <span style={{ color: "#00ff88", fontSize: 11 }}>✓ Завершено</span>
                      )}
                    </div>
                    <div style={{ fontFamily: "'Syne', sans-serif", fontSize: 16, fontWeight: 700, color: "#f1f5f9" }}>
                      {phase.title}
                    </div>
                    <div style={{ marginTop: 8, display: "flex", alignItems: "center", gap: 8 }}>
                      <div style={{ flex: 1, height: 3, background: "#1e2a3a", borderRadius: 2, overflow: "hidden" }}>
                        <div style={{
                          height: "100%", width: `${progress}%`,
                          background: `linear-gradient(90deg, ${phase.color}, ${phase.color}aa)`,
                          borderRadius: 2, transition: "width 0.4s ease",
                        }} />
                      </div>
                      <span style={{ color: "#475569", fontSize: 11, minWidth: 32 }}>{progress}%</span>
                    </div>
                  </div>

                  <span style={{
                    color: phase.color, fontSize: 18,
                    transform: isOpen ? "rotate(90deg)" : "rotate(0deg)",
                    transition: "transform 0.3s",
                  }}>›</span>
                </div>

                {/* Expanded content */}
                {isOpen && (
                  <div className="fade-in" style={{ borderTop: `1px solid ${phase.color}22`, padding: "24px" }}>
                    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 24 }}>

                      {/* Topics */}
                      <div>
                        <div style={{ color: "#64748b", fontSize: 11, letterSpacing: 2, marginBottom: 12 }}>
                          📚 ТЕМЫ ДЛЯ ИЗУЧЕНИЯ
                        </div>
                        {phase.topics.map((topic, ti) => {
                          const done = completedTopics[`${pi}-${ti}`];
                          return (
                            <div
                              key={ti}
                              className="topic-item"
                              onClick={() => toggleTopic(pi, ti)}
                              style={{
                                display: "flex", alignItems: "flex-start", gap: 10,
                                padding: "8px 10px", borderRadius: 6, marginBottom: 4,
                              }}
                            >
                              <div style={{
                                width: 16, height: 16, flexShrink: 0, marginTop: 1,
                                border: `1.5px solid ${done ? phase.color : "#334155"}`,
                                borderRadius: 4,
                                background: done ? phase.color : "transparent",
                                display: "flex", alignItems: "center", justifyContent: "center",
                                transition: "all 0.2s",
                              }}>
                                {done && <span style={{ color: "#0a0e1a", fontSize: 10, fontWeight: 700 }}>✓</span>}
                              </div>
                              <span style={{
                                fontSize: 13, color: done ? "#475569" : "#cbd5e1",
                                textDecoration: done ? "line-through" : "none",
                                lineHeight: 1.5,
                              }}>{topic}</span>
                            </div>
                          );
                        })}
                      </div>

                      {/* Tasks */}
                      <div>
                        <div style={{ color: "#64748b", fontSize: 11, letterSpacing: 2, marginBottom: 12 }}>
                          🛠️ ПРАКТИЧЕСКИЕ ЗАДАЧИ
                        </div>
                        {phase.tasks.map((task, ti) => {
                          const done = completedTasks[`${pi}-${ti}`];
                          return (
                            <div
                              key={ti}
                              className="task-item"
                              onClick={() => toggleTask(pi, ti)}
                              style={{
                                display: "flex", alignItems: "flex-start", gap: 10,
                                padding: "8px 10px", borderRadius: 6, marginBottom: 4,
                                border: `1px solid ${done ? phase.color + "44" : "rgba(255,255,255,0.04)"}`,
                                background: done ? `${phase.color}08` : "transparent",
                              }}
                            >
                              <div style={{
                                width: 16, height: 16, flexShrink: 0, marginTop: 1,
                                border: `1.5px solid ${done ? phase.color : "#334155"}`,
                                borderRadius: "50%",
                                background: done ? phase.color : "transparent",
                                display: "flex", alignItems: "center", justifyContent: "center",
                                transition: "all 0.2s",
                              }}>
                                {done && <span style={{ color: "#0a0e1a", fontSize: 9, fontWeight: 700 }}>✓</span>}
                              </div>
                              <span style={{
                                fontSize: 13, color: done ? "#475569" : "#e2e8f0",
                                textDecoration: done ? "line-through" : "none",
                                lineHeight: 1.5,
                              }}>{task}</span>
                            </div>
                          );
                        })}
                      </div>
                    </div>

                    {/* Resources */}
                    <div style={{ marginTop: 24 }}>
                      <div style={{ color: "#64748b", fontSize: 11, letterSpacing: 2, marginBottom: 12 }}>
                        🔗 РЕСУРСЫ ДЛЯ ПРОВЕРКИ ЗНАНИЙ
                      </div>
                      <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
                        {phase.resources.map((res, ri) => (
                          
                            key={ri}
                            href={res.url}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="resource-link"
                            style={{
                              display: "flex", alignItems: "center", gap: 8,
                              padding: "8px 14px",
                              borderRadius: 8,
                              background: "#111827",
                              border: `1px solid rgba(255,255,255,0.08)`,
                              color: "#e2e8f0",
                              fontSize: 13,
                            }}
                          >
                            <span style={{
                              background: `${typeColors[res.type] || "#64748b"}22`,
                              color: typeColors[res.type] || "#64748b",
                              border: `1px solid ${typeColors[res.type] || "#64748b"}44`,
                              borderRadius: 4,
                              padding: "1px 6px",
                              fontSize: 10,
                              fontWeight: 600,
                              letterSpacing: 0.5,
                            }}>{res.type}</span>
                            {res.name}
                            <span style={{ color: "#334155", fontSize: 11 }}>↗</span>
                          </a>
                        ))}
                      </div>
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>

        {/* Footer */}
        <div style={{
          marginTop: 40, padding: "20px 24px",
          border: "1px solid rgba(0,255,136,0.1)",
          borderRadius: 12, background: "#0d1220",
          display: "flex", alignItems: "center", gap: 16,
        }}>
          <span style={{ fontSize: 28 }}>💡</span>
          <div>
            <div style={{ color: "#00ff88", fontSize: 12, fontWeight: 600, marginBottom: 4 }}>СОВЕТ</div>
            <div style={{ color: "#64748b", fontSize: 13, lineHeight: 1.6 }}>
              Кликайте по фазам, чтобы раскрыть темы и задачи. Отмечайте прогресс по мере обучения. Рекомендуемое время: <span style={{ color: "#e2e8f0" }}>6–10 месяцев</span> при 1–2 часах в день.
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}