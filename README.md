### Authentication
This demo is using TriggerAuthentication, which is namespace scoped.  To scope to the entire cluster, use ClusterTriggerAuthentication.

### Triggers
* protocol: amqp
* queueName: test_q
* mode: QueueLength
* value: 100


### Example events from the ScaledObject
```
Normal  KEDAScalersStarted          21m                keda-operator  Started scalers watch
Normal  KEDAScaleTargetDeactivated  21m                keda-operator  Deactivated apps/v1.Deployment demo-keda/httpbin from 1 to 0
Normal  ScaledObjectReady           20m (x2 over 21m)  keda-operator  ScaledObject is ready for scaling
```

#### After publishing 200 messages to the queue, the httpbin deployment scaled up.
```
❯ kgp -o wide -lapp=httpbin
NAME                       READY   STATUS    RESTARTS   AGE   IP            NODE       NOMINATED NODE   READINESS GATES
httpbin-779c54bf49-rxbcp   1/1     Running   0          53s   172.18.0.7    minikube   <none>           <none>
httpbin-779c54bf49-tb885   1/1     Running   0          43s   172.18.0.10   minikube   <none>           <none>
```

#### Event showing the ScaledObject increasing the replicas then decreasing post consumption
```
  Normal  KEDAScaleTargetActivated    9m14s  keda-operator  Scaled apps/v1.Deployment demo-keda/httpbin from 0 to 1
  Normal  KEDAScaleTargetDeactivated  9s     keda-operator  Deactivated apps/v1.Deployment demo-keda/httpbin from 2 to 0
```

#### After the scale down event, there are 0 httpbin pods
```
❯ kgp -o wide -lapp=httpbin
No resources found in demo-keda namespace.
```
