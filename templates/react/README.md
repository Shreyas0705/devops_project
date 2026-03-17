# {{PROJECT_NAME}} (React + Vite + TypeScript)

## Prereqs
- Node.js 18+

## Run
```
npm install
npm run dev -- --host
```

## Build
```
npm run build
```

## Test
```
npm test
```

## Docker
```
docker build -t {{PROJECT_NAME}} .
docker run -p 4173:4173 {{PROJECT_NAME}}
```

## CI
See `.github/workflows/ci.yml` (install, test, build).
