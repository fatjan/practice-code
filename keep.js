exports.gatherAndDeleteUnused = async () => {
    const unused = await exports.getUnusedDeployedFunctions();
    if (unused.length === 0) return;
    await exports.removeFunctions(unused);
  };
  
  exports.removeFunctions = async (funcs) => {
    const calls = {};
    funcs.forEach((address) => {
      calls[address.key] = { address };
    });
  
    const parameters = {
      data: calls,
      context: { remove: true },
    };
  
    const app = initApp();
  
    const publisher = {
      protocol: 'fargate',
      image: app.config.deployImage,
    };
  
    return app.celery.callAsync(publisher, parameters, 'postback');
  };