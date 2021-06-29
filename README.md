### Authentication
This demo is using TriggerAuthentication, which is namespace scoped.  To scope to the entire cluster, use ClusterTriggerAuthentication.

### Example events from the ScaledObject
```
Normal  KEDAScalersStarted          21m                keda-operator  Started scalers watch
Normal  KEDAScaleTargetDeactivated  21m                keda-operator  Deactivated apps/v1.Deployment demo-keda/httpbin from 1 to 0
Normal  ScaledObjectReady           20m (x2 over 21m)  keda-operator  ScaledObject is ready for scaling
