using AlfaCoreDumped.Domain.Entities.CompanyResources;
using AlfaCoreDumped.Infrastructure.DbContext;
using Microsoft.EntityFrameworkCore;

namespace AlfaCoreDumped.Infrastructure.DbRepository
{
    public class AlfaRepository : IAlfaRepository
    {
        private readonly AlfaDbContext _dbContext;

        public AlfaRepository(AlfaDbContext dbContext)
        {
            _dbContext = dbContext;
        }

        public bool Save()
        {
            return _dbContext.SaveChanges() >= 0;
        }

        public Area GetArea(Guid areaId)
        {
            return _dbContext.Areas.Where(p => p.Id == areaId)
                .FirstOrDefault();
        }

        public void AddArea(Area area)
        {
            if (area == null)
            {
                throw new ArgumentNullException(nameof(area));
            }
            area.Id = Guid.NewGuid();
            _dbContext.Areas.Add(area);
        }
    }
}
