# {{PROJECT_NAME}} (.NET Web API)

## Prereqs
- .NET 8 SDK

## Run
```
dotnet run --project src/{{PROJECT_NAME}}.csproj
```

## Test
```
dotnet test
```

## Docker
```
docker build -t {{PROJECT_NAME}} .
docker run -p 8080:8080 {{PROJECT_NAME}}
```

## CI
See `.github/workflows/ci.yml` (restore, build, test).
